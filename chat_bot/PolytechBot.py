import sqlite3
import telebot
from telebot import types
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Создаем соединение с базой данных SQLite для пользователей
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Создаем таблицу для хранения информации о пользователях и администраторах
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        is_admin INTEGER
    )
''')
conn.commit()

# Создаем соединение с базой данных SQLite для вопросов
questions_conn = sqlite3.connect('questions.db')
questions_cursor = questions_conn.cursor()

questions_cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
    )
''')
questions_conn.close()

# Получите токен бота от BotFather в Telegram
TOKEN = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'
bot = telebot.TeleBot(TOKEN)

# Функция для добавления пользователя в базу данных с is_admin = 1
def add_user(user_id):
    cursor.execute('INSERT OR IGNORE INTO users (id, is_admin) VALUES (?, 0)', (user_id,))
    conn.commit()

# Функция для проверки, является ли пользователь администратором
def is_user_admin(user_id):
    cursor.execute('SELECT * FROM users WHERE id=? AND is_admin=1', (user_id,))
    return cursor.fetchone() is not None

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    user_id = message.from_user.id
    add_user(user_id)
    is_admin = is_user_admin(user_id)

    if is_admin:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
        markup.add(telebot.types.KeyboardButton("/showdb"))
        markup.add(telebot.types.KeyboardButton("/addadmin"))
        markup.add(telebot.types.KeyboardButton("/questions"))
        bot.send_message(user_id, "Привет! Я ваш бот.", reply_markup=markup)
    else:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
        markup.add(telebot.types.KeyboardButton("/questions"))
        markup.add(telebot.types.KeyboardButton("Обратная связь"))
        bot.send_message(user_id, "Привет! Я ваш бот.", reply_markup=markup)

# Обработчик команды "Обратная связь"
@bot.message_handler(func=lambda message: message.text == "Обратная связь")
def feedback_handler(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Напишите вашу почту для обратной связи:")
    bot.register_next_step_handler(message, ask_email)

# Обработчик получения почты от пользователя
def ask_email(message):
    user_id = message.from_user.id
    email = message.text
    bot.send_message(user_id, "Теперь напишите ваш вопрос:")
    bot.register_next_step_handler(message, lambda msg: ask_question(msg, email))

# Обработчик получения вопроса и отправка обратной связи на почту
def ask_question(message, email):
    user_id = message.from_user.id
    question = message.text
    send_feedback(email, question)
    bot.send_message(user_id, "Спасибо за ваш вопрос! Мы ответим вам в ближайшее время.")

# Функция для отправки обратной связи на почту
def send_feedback(email, question):
    # Замените следующие параметры своими данными
    sender_email = "tetenkinevgenij@gmail.com"
    sender_password = "gsgt vuei xxqr kmer"
    receiver_email = "anatolevicanatolij560@gmail.com"

    # Формируем сообщение
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Обратная связь от пользователя'

    body = f"Email пользователя: {email}\n\nВопрос:\n{question}"
    msg.attach(MIMEText(body, 'plain'))

    # Отправляем сообщение через SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Обработчик команды /showdb
@bot.message_handler(commands=['showdb'])
def show_db_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        cursor.execute('SELECT * FROM users')
        db_content = cursor.fetchall()
        bot.send_message(user_id, "Содержимое базы данных:\n" + "\n".join(map(str, db_content)))
    else:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")

# Обработчик команды /addadmin
@bot.message_handler(commands=['addadmin'])
def add_admin_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        users = get_non_admin_users()  # Получаем список пользователей, не являющихся админами
        if users:
            markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
            for user in users:
                markup.add(telebot.types.KeyboardButton(str(user)))
            markup.add(telebot.types.KeyboardButton("Отмена"))
            bot.send_message(user_id, "Выберите пользователя, чтобы сделать его администратором:", reply_markup=markup)
            bot.register_next_step_handler(message, process_admin_choice)
        else:
            bot.send_message(user_id, "Нет пользователей для добавления в администраторы.")
    else:
        bot.send_message(user_id, "У вас нет прав для выполнения этой команды.")
# Функция для добавления пользователя в базу данных с is_admin = 1
def add_admin(user_id):
    cursor.execute('UPDATE users SET is_admin=1 WHERE id=?', (user_id,))
    conn.commit()

# Обработчик выбора пользователя и добавления его в администраторы
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

# Функция для получения списка всех пользователей, не являющихся админами
def get_non_admin_users():
    cursor.execute('SELECT id FROM users WHERE is_admin=0')
    users = cursor.fetchall()
    return [user[0] for user in users]

# Обработчик команды /questions
@bot.message_handler(commands=['questions'])
def show_questions_handler(message):
    user_id = message.from_user.id

    questions_conn = sqlite3.connect('questions.db')
    questions_cursor = questions_conn.cursor()

    questions_cursor.execute('SELECT * FROM questions')
    questions_content = questions_cursor.fetchall()

    questions_conn.close()

    if questions_content:
        formatted_questions = "\n".join([f"ID: {question[0]}, Text: {question[1]}" for question in questions_content])
        bot.send_message(user_id, "Содержимое базы данных вопросов:\n" + formatted_questions)
    else:
        bot.send_message(user_id, "База данных вопросов пуста.")

# Запускаем бота
bot.polling(none_stop=True)
