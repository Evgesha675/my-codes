import sqlite3
import io
import pandas as pd
import openpyxl
import yagmail
import keyring
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Document
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# Configuring logging
logging.basicConfig(filename='bot.log', level=logging.ERROR)

# Database setup
conn = sqlite3.connect('faqBot.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        is_admin INTEGER
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Topics (
        topic_id INTEGER PRIMARY KEY,
        topic_name TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Questions (
        question_id INTEGER PRIMARY KEY,
        topic_id INTEGER,
        question_text TEXT,
        FOREIGN KEY (topic_id) REFERENCES Topics(topic_id)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Answers (
        answer_id INTEGER PRIMARY KEY,
        question_id INTEGER,
        answer_text TEXT,
        FOREIGN KEY (question_id) REFERENCES Questions(question_id)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FrequentlyAskedRequests (
        request_id INTEGER PRIMARY KEY,
        request_text TEXT,
        response_text TEXT
    )
''')
conn.commit()

# Bot setup
TOKEN = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# States for FSM
class RequestForm(StatesGroup):
    waiting_for_request_type = State()
    waiting_for_request = State()
    waiting_for_email = State()
    waiting_for_phone = State()

class QAForm(StatesGroup):
    waiting_for_topic_choice = State()
    waiting_for_question_choice = State()

class AdminForm(StatesGroup):
    waiting_for_admin_choice = State()

# Function to add a user to the database
async def add_user(user_id):
    with conn:
        cursor.execute('INSERT OR IGNORE INTO users (id, is_admin) VALUES (?, 0)', (user_id,))

# Function to add admin privileges to a user
async def add_admin(user_id):
    cursor.execute('UPDATE users SET is_admin=1 WHERE id=?', (user_id,))
    conn.commit()

# Function to check if a user is an admin
async def is_user_admin(user_id):
    cursor.execute('SELECT is_admin FROM users WHERE id=?', (user_id,))
    result = cursor.fetchone()
    return result and result[0] == 1

@dp.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await add_user(user_id)
    is_admin = await is_user_admin(user_id)

    # Определяем кнопки в зависимости от статуса пользователя
    if is_admin:
        buttons = [
            [KeyboardButton(text="Show usersDB"), KeyboardButton(text="Add admin")],
            [KeyboardButton(text="Show QA"), KeyboardButton(text="Change QA")]
        ]
    else:
        buttons = [
            [KeyboardButton(text="Make a request for document"), KeyboardButton(text="Show QA")]
        ]

    # Инициализация ReplyKeyboardMarkup сразу с кнопками
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    # Отправляем ответ пользователю с кнопками
    await message.answer("How can I help you?", reply_markup=markup)





@dp.message(lambda message: message.text == 'Make a request for document')
async def make_document_request(message: types.Message, state: FSMContext):
    cursor.execute('SELECT request_text FROM FrequentlyAskedRequests')
    far_data = cursor.fetchall()

    if not far_data:
        await message.answer("No frequently asked requests available.")
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for row in far_data:
            markup.add(row[0])
        markup.add("Another request", "Cancel")
        await message.answer("Choose a frequently asked request or select 'Another request':", reply_markup=markup)
        await state.set_state(RequestForm.waiting_for_request_type)

@dp.message(RequestForm.waiting_for_request_type)
async def process_selected_request_or_another(message: types.Message, state: FSMContext):
    selected_option = message.text.strip().lower()

    if selected_option == 'cancel':
        await start_handler(message, state)
    elif selected_option == 'another request':
        await message.answer("Write your request:")
        await state.set_state(RequestForm.waiting_for_request)
    else:
        await state.update_data(request=selected_option)
        await message.answer(f"Your request '{selected_option}' has been received. Please enter your email:")
        await state.set_state(RequestForm.waiting_for_email)

@dp.message(RequestForm.waiting_for_request)
async def process_another_request(message: types.Message, state: FSMContext):
    if message.text.strip().lower() == 'cancel':
        await start_handler(message, state)
    else:
        await state.update_data(request=message.text)
        await message.answer("Enter your email:")
        await state.set_state(RequestForm.waiting_for_email)

@dp.message(RequestForm.waiting_for_email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text.strip()
    if email.lower() == 'cancel':
        await start_handler(message, state)
        return
    await state.update_data(email=email)
    await message.answer("Please enter your phone number:")
    await state.set_state(RequestForm.waiting_for_phone)

@dp.message(RequestForm.waiting_for_phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text.strip()
    if phone.lower() == 'cancel':
        await start_handler(message, state)
        return
    user_data = await state.get_data()
    await send_email_to_dean_office(user_data['request'], user_data['email'], phone)
    await message.answer(f"Your request '{user_data['request']}' with email '{user_data['email']}' and phone number '{phone}' has been successfully sent!")
    await start_handler(message, state)

# Command handler for showing QA (Frequently Asked Questions)
@dp.message(lambda message: message.text == 'Show QA')
async def show_QA_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await is_user_admin(user_id):
        cursor.execute('''
            SELECT Topics.topic_name, Questions.question_text, Answers.answer_text
            FROM Topics
            LEFT JOIN Questions ON Topics.topic_id = Questions.topic_id
            LEFT JOIN Answers ON Questions.question_id = Answers.question_id
        ''')
        faq_data = cursor.fetchall()

        if not faq_data:
            await message.answer("No FAQ data available.")
        else:
            formatted_data = ""
            current_topic = None

            for row in faq_data:
                topic_name, question_text, answer_text = row
                if topic_name != current_topic:
                    formatted_data += f"\n\n*{topic_name}*"
                    current_topic = topic_name
                formatted_data += f"\n\n• {question_text}\n  - {answer_text}"

            await message.answer(formatted_data, parse_mode="Markdown")
    else:
        cursor.execute('SELECT DISTINCT topic_name FROM Topics')
        topics = cursor.fetchall()

        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for topic in topics:
            markup.add(topic[0])
        markup.add("Cancel")

        await message.answer("Select a topic:", reply_markup=markup)
        await state.set_state(QAForm.waiting_for_topic_choice)

@dp.message(QAForm.waiting_for_topic_choice)
async def process_user_topic_choice(message: types.Message, state: FSMContext):
    selected_topic_name = message.text.strip().lower()
    if selected_topic_name == 'cancel':
        await start_handler(message, state)
        return

    cursor.execute('SELECT topic_id FROM Topics WHERE topic_name=?', (selected_topic_name,))
    selected_topic_id = cursor.fetchone()[0]

    cursor.execute('SELECT question_text FROM Questions WHERE topic_id=?', (selected_topic_id,))
    questions = cursor.fetchall()

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for question in questions:
        markup.add(question[0])
    markup.add("Cancel")

    await message.answer("Select a question:", reply_markup=markup)
    await state.set_state(QAForm.waiting_for_question_choice)

@dp.message(QAForm.waiting_for_question_choice)
async def process_user_question_choice(message: types.Message, state: FSMContext):
    selected_question_text = message.text.strip().lower()
    if selected_question_text == 'cancel':
        await show_QA_handler(message, state)
        return

    cursor.execute(
        'SELECT answer_text FROM Answers WHERE question_id IN (SELECT question_id FROM Questions WHERE question_text=?)',
        (selected_question_text,))
    answer = cursor.fetchone()[0]

    await message.answer(f"{answer}")
    await start_handler(message, state)

@dp.message(lambda message: message.text == 'Add admin')
async def add_admin_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await is_user_admin(user_id):
        cursor.execute('SELECT id FROM users WHERE is_admin=0')
        users = cursor.fetchall()

        if users:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for user in users:
                markup.add(str(user[0]))
            markup.add("Cancel")

            await message.answer("Select a user to make him an administrator:", reply_markup=markup)
            await state.set_state(AdminForm.waiting_for_admin_choice)
        else:
            await message.answer("There are no users to add as administrators.")
    else:
        await message.answer("You do not have permission to execute this command.")

@dp.message(AdminForm.waiting_for_admin_choice)
async def process_admin_choice(message: types.Message, state: FSMContext):
    selected_user_id = message.text.strip().lower()
    if selected_user_id == 'cancel':
        await start_handler(message, state)
        return

    try:
        selected_user_id = int(selected_user_id)
        await add_admin(selected_user_id)
        await message.answer(f"User with ID {selected_user_id} has been added to administrators.")
    except ValueError:
        await message.answer("Please select the correct user.")

@dp.message(lambda message: message.text == 'Show usersDB')
async def show_db_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await is_user_admin(user_id):
        cursor.execute('SELECT * FROM users')
        db_content = cursor.fetchall()
        await message.answer("Database contents:\n" + "\n".join(map(str, db_content)))
    else:
        await message.answer("You do not have permission to execute this command.")

# Function to generate Excel file from the database
async def generate_excel_file():
    cursor.execute('''
        SELECT Topics.topic_name, Questions.question_text, Answers.answer_text
        FROM Topics
        LEFT JOIN Questions ON Topics.topic_id = Questions.topic_id
        LEFT JOIN Answers ON Questions.question_id = Answers.question_id
    ''')
    faq_data = cursor.fetchall()

    if not faq_data:
        return None

    df = pd.DataFrame(faq_data, columns=['Topic', 'Question', 'Answer'])
    excel_data = io.BytesIO()
    df.to_excel(excel_data, index=False, sheet_name='FAQ')
    excel_data.seek(0)
    return excel_data

@dp.message(lambda message: message.text == 'Change QA')
async def redact_bd_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if await is_user_admin(user_id):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add("Cancel")

        excel_data = await generate_excel_file()
        if excel_data:
            await message.answer_document(types.InputFile(excel_data, 'FAQ.xlsx'), caption="Edit the file and send it back to update the database.", reply_markup=markup)
            await state.set_state(QAForm.waiting_for_question_choice)
        else:
            await message.answer("There is no data to create a file.")
    else:
        await message.answer("You do not have permission to execute this command.")

@dp.message(QAForm.waiting_for_question_choice)
async def process_edited_excel_file(message: types.Message, state: FSMContext):
    if message.text.strip().lower() == 'cancel':
        await start_handler(message, state)
    elif message.document:
        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_data = await bot.download_file(file.file_path)

        await update_database_from_excel(file_data)
        await message.answer("The database has been successfully updated.")
    else:
        await message.answer("Please send an Excel file to update the database.")

async def update_database_from_excel(file_data):
    try:
        df = pd.read_excel(io.BytesIO(file_data), engine='openpyxl')

        cursor.execute('DELETE FROM Topics')
        cursor.execute('DELETE FROM Questions')
        cursor.execute('DELETE FROM Answers')
        conn.commit()

        for _, row in df.iterrows():
            topic_name = row['Topic']
            question_text = row['Question']
            answer_text = row['Answer']

            cursor.execute('INSERT OR IGNORE INTO Topics (topic_name) VALUES (?)', (topic_name,))
            conn.commit()

            cursor.execute('SELECT topic_id FROM Topics WHERE topic_name=?', (topic_name,))
            topic_id = cursor.fetchone()[0]

            cursor.execute('INSERT INTO Questions (topic_id, question_text) VALUES (?, ?)', (topic_id, question_text))
            conn.commit()

            cursor.execute('SELECT question_id FROM Questions WHERE topic_id=? AND question_text=?', (topic_id, question_text))
            question_id = cursor.fetchone()[0]

            cursor.execute('INSERT INTO Answers (question_id, answer_text) VALUES (?, ?)', (question_id, answer_text))
            conn.commit()

    except Exception as e:
        print(f"An error occurred when updating the database from an Excel file: {e}")

async def send_email_to_dean_office(question, email, phone):
    sender_email = "my_mail"
    dean_office_email = "deans_office_mail"
    subject = "New request for documents"
    body = f"Request: {question}\nEmail: {email}\nPhone number: {phone}"
    sender_password = "mail_password"

    yagmail.register(sender_email, sender_password)
    yag = yagmail.SMTP(sender_email)
    yag.send(to=dean_office_email, subject=subject, contents=body)
    yag.close()

if __name__ == "__main__":
    dp.run_polling(bot, skip_updates=True)
