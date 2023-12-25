import sqlite3
import telebot
import io
import pandas as pd
import openpyxl
import yagmail
import smtplib
import os
import base64
import keyring


conn = sqlite3.connect('faqBot.db', check_same_thread=False)
cursor = conn.cursor()

# creating users_db
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        is_admin INTEGER
    )
''')

# creating Topics_db
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Topics (
        topic_id INTEGER PRIMARY KEY,
        topic_name TEXT
    )
''')

# creating Questions_Topics_db
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Questions (
        question_id INTEGER PRIMARY KEY,
        topic_id INTEGER,
        question_text TEXT,
        FOREIGN KEY (topic_id) REFERENCES Topics(topic_id)
    )
''')

# creating Answers_Questions_Topics_db
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Answers (
        answer_id INTEGER PRIMARY KEY,
        question_id INTEGER,
        answer_text TEXT,
        FOREIGN KEY (question_id) REFERENCES Questions(question_id)
    )
''')

conn.commit()

# creating FAR
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FrequentlyAskedRequests (
        request_id INTEGER PRIMARY KEY,
        request_text TEXT,
        response_text TEXT
    )
''')
conn.commit()


TOKEN = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'
bot = telebot.TeleBot(TOKEN)
markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)


def add_user(user_id):
    with conn:
        new_cursor = conn.cursor()
        new_cursor.execute('INSERT OR IGNORE INTO users (id, is_admin) VALUES (?, 0)', (user_id,))



def add_admin(user_id):
    cursor.execute('UPDATE users SET is_admin=1 WHERE id=?', (user_id,))
    conn.commit()

def is_user_admin(user_id):
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT is_admin FROM users WHERE id=?', (user_id,))
        result = cursor.fetchone()
    return result and result[0] == 1



@bot.message_handler(commands=['start'])
def start_handler(message):
    user_id = message.from_user.id
    add_user(user_id)
    is_admin = is_user_admin(user_id)

    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  # Create a new markup instance

    if is_admin:
        markup.add(telebot.types.KeyboardButton("Show usersDB"))
        markup.add(telebot.types.KeyboardButton("Add admin"))
        markup.add(telebot.types.KeyboardButton("Show qaDB"))
        markup.add(telebot.types.KeyboardButton("Change qaDB"))
        bot.send_message(user_id, "Welcome! \nHow can i help you?", reply_markup=markup)
    else:
        user_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        user_markup.add(telebot.types.KeyboardButton("Make a request for document"))
        user_markup.add(telebot.types.KeyboardButton("Show qaDB"))
        bot.send_message(user_id, "Welcome! \nHow can i help you?", reply_markup=user_markup)




# Команда /make_document_request
@bot.message_handler(func=lambda message: message.text == 'Make a request for document')
def make_document_request(message):
    user_id = message.from_user.id

    cursor.execute('SELECT request_text FROM FrequentlyAskedRequests')
    far_data = cursor.fetchall()

    if not far_data:
        bot.send_message(user_id, "No frequently asked requests available.")
    else:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for row in far_data:
            markup.add(telebot.types.KeyboardButton(row[0]))

        markup.add(telebot.types.KeyboardButton("Another request"))
        markup.add(telebot.types.KeyboardButton("Cancel"))
        bot.send_message(user_id, "Choose a frequently asked request or select 'Another request':", reply_markup=markup)
        bot.register_next_step_handler(message, process_selected_request_or_another)

def process_selected_request_or_another(message):
    user_id = message.from_user.id
    selected_option = message.text

    if selected_option.lower() == 'cancel':
        start_handler(message)
    elif selected_option.lower() == 'another request':
        bot.send_message(user_id, "Write your request:")
        bot.register_next_step_handler(message, process_another_request)
    else:
        # Здесь можно вставить код для отправки запроса на почту для выбранной опции FAR
        bot.send_message(user_id, f"Your request '{selected_option}' has been received. Please enter your email:")
        bot.register_next_step_handler(message, process_email, request=selected_option)

def process_another_request(message):
    user_id = message.from_user.id
    if message.text.lower() == 'cancel':
        start_handler(message)
    else:
        question = message.text
        bot.send_message(user_id, "Enter your email:")
        bot.register_next_step_handler(message, process_email, request=question)

def process_email(message, request):
    user_id = message.from_user.id
    email = message.text

    # Здесь можно добавить код для отправки email и запроса на почту
    bot.send_message(user_id, "Please enter your phone number:")
    bot.register_next_step_handler(message, process_phone, request=request, email=email)

def process_phone(message, request, email):
    user_id = message.from_user.id
    phone = message.text

    # Отправляем данные на почту деканата
    send_email_to_dean_office(request, email, phone)

    # Сообщаем пользователю о успешной отправке запроса
    bot.send_message(user_id, f"Your request '{request}' with email '{email}' and phone number '{phone}'has been deleted xD Sasay lalka")

    # Возвращаем пользователя в начальное меню
    start_handler(message)


# Функция для отправки email на почту деканата
def send_email_to_dean_office(question, email, phone):
    sender_email = "tetenkinevgenij@gmail.com"
    dean_office_email = "telegrambricks@gmail.com"

    subject = "New request for documents"
    body = f"Request: {question}\nEmail: {email}\nPhone number: {phone}"

    #get pass (feauture)
    sender_password = "here is a password "

    # Отправка письма с использованием пароля
    yagmail.register(sender_email, sender_password)
    yag = yagmail.SMTP(sender_email)
    yag.send(to=dean_office_email, subject=subject, contents=body)
    yag.close()

    print(f"Your request ({question}) ")









# Команда /show_qaDB
@bot.message_handler(func=lambda message: message.text.lower() == 'show qadb')
def show_qaDB_handler(message):
    user_id = message.from_user.id
    try:
        cursor.execute('SELECT DISTINCT topic_name FROM Topics')
        topics = cursor.fetchall()

        markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        for topic in topics:
            markup.add(telebot.types.KeyboardButton(topic[0]))
        markup.add(telebot.types.KeyboardButton("Cancel"))

        bot.send_message(user_id, "Select a topic:", reply_markup=markup)
        bot.register_next_step_handler(message, process_user_topic_choice)
    except Exception as e:
        print(e)
        bot.send_message(user_id, "An error occurred. Please try again.")


def process_user_topic_choice(message):
    user_id = message.from_user.id
    try:
        selected_topic_name = message.text
        if selected_topic_name.lower() == 'cancel':
            start_handler(message)
            return

        cursor.execute('SELECT topic_id FROM Topics WHERE topic_name=?', (selected_topic_name,))
        selected_topic_id = cursor.fetchone()[0]

        cursor.execute('SELECT question_text FROM Questions WHERE topic_id=?', (selected_topic_id,))
        questions = cursor.fetchall()

        markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        for question in questions:
            markup.add(telebot.types.KeyboardButton(question[0]))
        markup.add(telebot.types.KeyboardButton("Cancel"))

        bot.send_message(user_id, "Select a question:", reply_markup=markup)
        bot.register_next_step_handler(message, process_user_question_choice)
    except Exception as e:
        print(e)
        bot.send_message(user_id, "Invalid input. Please select a valid topic.")

def process_user_question_choice(message):
    user_id = message.from_user.id
    try:
        selected_question_text = message.text
        if selected_question_text.lower() == 'cancel':
            show_qaDB_handler(message)
            return

        cursor.execute('SELECT answer_text FROM Answers WHERE question_id IN (SELECT question_id FROM Questions WHERE question_text=?)', (selected_question_text,))
        answer = cursor.fetchone()[0]

        bot.send_message(user_id, f"Question: {selected_question_text}\nAnswer: {answer}")

        # Возвращаем пользователя в начальное меню
        start_handler(message)
    except Exception as e:
        print(e)
        bot.send_message(user_id, "Invalid input. Please select a valid question.")




@bot.message_handler(func=lambda message: message.text == 'Add admin')
def add_admin_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        users = get_non_admin_users()

        if users:
            markup = telebot.types.ReplyKeyboardMarkup(row_width=1)  # Create a new markup instance
            for user in users:
                markup.add(telebot.types.KeyboardButton(str(user)))
            markup.add(telebot.types.KeyboardButton("Отмена"))
            
            if message.text == "Отмена":
                start_handler(message)
            else:
                bot.send_message(user_id, "Select a user to make him an administrator:", reply_markup=markup)
                bot.register_next_step_handler(message, process_admin_choice)
        else:
            bot.send_message(user_id, "Нет пользователей для добавления в администраторы.")
    else:
        bot.send_message(user_id, "You do not have permission to execute this command.")

def get_non_admin_users():
    cursor.execute('SELECT id FROM users WHERE is_admin=0')
    users = cursor.fetchall()
    return [user[0] for user in users]


def process_admin_choice(message):
    user_id = message.from_user.id
    if message.text == "Отмена":
        start_handler(message)
    else:
        try:
            selected_user_id = int(message.text)
            add_admin(selected_user_id)
            bot.send_message(user_id, f"Пользователь с ID {selected_user_id} добавлен в администраторы.")
        except ValueError:
            bot.send_message(user_id, "Пожалуйста, выберите корректного пользователя.")


@bot.message_handler(func=lambda message: message.text == 'Show usersDB')
def show_db_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        cursor.execute('SELECT * FROM users')
        db_content = cursor.fetchall()
        bot.send_message(user_id, "Содержимое базы данных:\n" + "\n".join(map(str, db_content)))
    else:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")


# Function to generate Excel file from the database
def generate_excel_file():
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



# Command to request the Excel file for redaction
@bot.message_handler(func=lambda message: message.text == 'Change qaDB')
def redact_bd_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        markup.add(telebot.types.KeyboardButton("Cancel"))
        
        excel_data = generate_excel_file()
        if excel_data:
            bot.send_document(user_id, excel_data, caption="Редактируйте файл и отправьте его обратно для обновления базы данных.", reply_markup=markup)
            bot.register_next_step_handler(message, process_edited_excel_file)
        else:
            bot.send_message(user_id, "Нет данных для создания файла.")
    else:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")

@bot.message_handler(func=lambda message: message.text == 'Cancel')
def cancel_handler(message):
    start_handler(message)



def process_edited_excel_file(message):
    user_id = message.from_user.id
    if message.text == 'Cancel':
        start_handler(message)
    elif message.document:
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        file_data = bot.download_file(file_info.file_path)

        # Обновить базу данных из редактированного Excel-файла
        update_database_from_excel(file_data)

        bot.send_message(user_id, "База данных успешно обновлена.")
    else:
        bot.send_message(user_id, "Пожалуйста, отправьте файл Excel для обновления базы данных.")


# Function to update the database from the edited Excel file
def update_database_from_excel(file_data):
    try:
        df = pd.read_excel(file_data, engine='openpyxl')

        # Очищаем существующие данные в таблицах
        cursor.execute('DELETE FROM Topics')
        cursor.execute('DELETE FROM Questions')
        cursor.execute('DELETE FROM Answers')
        conn.commit()

        # Заполняем базу данных из DataFrame
        for _, row in df.iterrows():
            topic_name = row['Topic']
            question_text = row['Question']
            answer_text = row['Answer']

            # Добавляем тему, если её ещё нет
            cursor.execute('INSERT OR IGNORE INTO Topics (topic_name) VALUES (?)', (topic_name,))
            conn.commit()

            # Получаем id темы
            cursor.execute('SELECT topic_id FROM Topics WHERE topic_name=?', (topic_name,))
            topic_id = cursor.fetchone()[0]

            # Добавляем вопрос
            cursor.execute('INSERT INTO Questions (topic_id, question_text) VALUES (?, ?)', (topic_id, question_text))
            conn.commit()

            # Получаем id вопроса
            cursor.execute('SELECT question_id FROM Questions WHERE topic_id=? AND question_text=?', (topic_id, question_text))
            question_id = cursor.fetchone()[0]

            # Добавляем ответ
            cursor.execute('INSERT INTO Answers (question_id, answer_text) VALUES (?, ?)', (question_id, answer_text))
            conn.commit()

        print("База данных успешно обновлена.")
    except Exception as e:
        print(f"Произошла ошибка при обновлении базы данных из Excel файла: {e}")
        # Обработка ошибок, например, уведомление администратора о некорректном формате файла


# Start the bot
bot.polling(none_stop=True)