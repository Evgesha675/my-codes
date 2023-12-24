import sqlite3
import telebot
import io
import pandas as pd
import openpyxl
import yagmail
import smtplib
import os
import base64

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

TOKEN = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'
bot = telebot.TeleBot(TOKEN)
markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)


def add_user(user_id):
    cursor.execute('INSERT OR IGNORE INTO users (id, is_admin) VALUES (?, 0)', (user_id,))
    conn.commit()


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
        markup.add(telebot.types.KeyboardButton("/showdb"))
        markup.add(telebot.types.KeyboardButton("/addadmin"))
        markup.add(telebot.types.KeyboardButton("/show_all_data"))
        markup.add(telebot.types.KeyboardButton("/redact_bd"))
        bot.send_message(user_id, "Привет! Я ваш бот.", reply_markup=markup)
    else:
        user_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        user_markup.add(telebot.types.KeyboardButton("/make_document_request"))
        user_markup.add(telebot.types.KeyboardButton("/show_all_data"))
        bot.send_message(user_id, "Welcome! \n How can i help you?", reply_markup=user_markup)





# Команда /make_document_request
@bot.message_handler(commands=['make_document_request'])
def make_document_request(message):
    user_id = message.from_user.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    # Добавляем кнопки "Frequently asked questions" и "Another request"
    markup.add(telebot.types.KeyboardButton("/frequently_asked_questions"))
    markup.add(telebot.types.KeyboardButton("/another_request"))

    bot.send_message(user_id, "Выберите действие:", reply_markup=markup)

# Команда /frequently_asked_questions
@bot.message_handler(commands=['frequently_asked_questions'])
def frequently_asked_questions(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Здесь будет текст часто задаваемых вопросов, когда они будут добавлены.")

# Команда /another_request
@bot.message_handler(commands=['another_request'])
def another_request(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Введите ваш вопрос:")
    bot.register_next_step_handler(message, process_another_request)

# Функция для обработки дополнительного запроса
def process_another_request(message):
    user_id = message.from_user.id
    question = message.text

    # Задаем вопросы по email и телефону
    bot.send_message(user_id, "Введите ваш email:")
    bot.register_next_step_handler(message, process_email, question=question)

# Функция для обработки email
def process_email(message, question):
    user_id = message.from_user.id
    email = message.text

    # Задаем вопросы по телефону
    bot.send_message(user_id, "Введите ваш номер телефона:")
    bot.register_next_step_handler(message, process_phone, question=question, email=email)

# Функция для обработки номера телефона
def process_phone(message, question, email):
    user_id = message.from_user.id
    phone = message.text

    # Отправляем данные на почту деканата
    send_email_to_dean_office(question, email, phone)

    bot.send_message(user_id, "Ваш запрос успешно отправлен.")

# Функция для отправки email на почту деканата
def send_email_to_dean_office(question, email, phone):
    sender_email = "tetenkinevgenij@gmail.com"
    dean_office_email = "telegrambricks@gmail.com"

    subject = "Новый запрос на документы"
    body = f"Вопрос: {question}\nEmail: {email}\nТелефон: {phone}"

    # Запрос пароля через input
    sender_password = input("Введите пароль для {}:".format(sender_email))

    # Отправка письма с использованием пароля
    yagmail.register(sender_email, sender_password)
    yag = yagmail.SMTP(sender_email)
    yag.send(to=dean_office_email, subject=subject, contents=body)
    yag.close()

    print("Письмо успешно отправлено.")






@bot.message_handler(commands=['show_all_data'])
def get_all_faq_data(message):
    user_id = message.from_user.id

    cursor.execute('''
        SELECT Topics.topic_name, Questions.question_text, Answers.answer_text
        FROM Topics
        LEFT JOIN Questions ON Topics.topic_id = Questions.topic_id
        LEFT JOIN Answers ON Questions.question_id = Answers.question_id
    ''')
    faq_data = cursor.fetchall()
    print("FAQ data:", faq_data)

    if not faq_data:
        bot.send_message(user_id, "No FAQ data available.")
    else:
        formatted_data = ""
        current_topic = None

        for row in faq_data:
            topic_name, question_text, answer_text = row
            if topic_name != current_topic:
                formatted_data += f"\n\n*{topic_name}*"
                current_topic = topic_name
            formatted_data += f"\n\n• {question_text}\n  - {answer_text}"

        bot.send_message(user_id, formatted_data, parse_mode="Markdown")



@bot.message_handler(commands=['addadmin'])
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
                bot.send_message(user_id, "Выберите пользователя, чтобы сделать его администратором:", reply_markup=markup)
                bot.register_next_step_handler(message, process_admin_choice)
        else:
            bot.send_message(user_id, "Нет пользователей для добавления в администраторы.")
    else:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")

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


@bot.message_handler(commands=['showdb'])
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
@bot.message_handler(commands=['redact_bd'])
def redact_bd_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        excel_data = generate_excel_file()
        if excel_data:
            bot.send_document(user_id, excel_data, caption="Редактируйте файл и отправьте его обратно для обновления базы данных.")
            bot.register_next_step_handler(message, process_edited_excel_file)
        else:
            bot.send_message(user_id, "Нет данных для создания файла.")
    else:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")


def process_edited_excel_file(message):
    user_id = message.from_user.id
    if message.document:
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