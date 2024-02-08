# Importing necessary libraries
import sqlite3
import telebot
import io
import pandas as pd
import openpyxl
import yagmail
import smtplib as SMTP
import os
import base64
import keyring
import logging
import time

# Configuring logging
logging.basicConfig(filename='bot.log', level=logging.ERROR)

# Connectin`g to SQLite database
with sqlite3.connect('faqBot.db', check_same_thread=False) as conn:
    cursor = conn.cursor()

    # Creating users_db table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            is_admin INTEGER
        )
    ''')

    # Creating Topics_db table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Topics (
            topic_id INTEGER PRIMARY KEY,
            topic_name TEXT
        )
    ''')

    # Creating Questions_Topics_db table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Questions (
            question_id INTEGER PRIMARY KEY,
            topic_id INTEGER,
            question_text TEXT,
            FOREIGN KEY (topic_id) REFERENCES Topics(topic_id)
        )
    ''')

    # Creating Answers_Questions_Topics_db table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Answers (
            answer_id INTEGER PRIMARY KEY,
            question_id INTEGER,
            answer_text TEXT,
            FOREIGN KEY (question_id) REFERENCES Questions(question_id)
        )
    ''')

    # Creating FaR table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FrequentlyAskedRequests (
            request_id INTEGER PRIMARY KEY,
            request_text TEXT,
            response_text TEXT
        )
    ''')

    # Committing changes to the database
    conn.commit()

# Bot token``
TOKEN = 'token'
bot = telebot.TeleBot(TOKEN)

# Reply keyboard markup
markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
# Function to add a user to the database
def add_user(user_id):
    with conn:
        new_cursor = conn.cursor()
        new_cursor.execute('INSERT OR IGNORE INTO users (id, is_admin) VALUES (?, 0)', (user_id,))

# Function to add admin privileges to a user
def add_admin(user_id):
    cursor.execute('UPDATE users SET is_admin=1 WHERE id=?', (user_id,))
    conn.commit()

# Function to check if a user is an admin
def is_user_admin(user_id):
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT is_admin FROM users WHERE id=?', (user_id,))
        result = cursor.fetchone()
    return result and result[0] == 1

# Command handler for '/start'
@bot.message_handler(commands=['start'])
def start_handler(message):
    user_id = message.from_user.id
    add_user(user_id)
    is_admin = is_user_admin(user_id)

    # Reply keyboard markup for admin and non-admin users
    if is_admin:
        markup.add(telebot.types.KeyboardButton("Show usersDB"))
        markup.add(telebot.types.KeyboardButton("Add admin"))
        markup.add(telebot.types.KeyboardButton("Show QA"))
        markup.add(telebot.types.KeyboardButton("Change QA"))
        bot.send_message(user_id, "How can I help you?", reply_markup=markup)
    else:
        user_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        user_markup.add(telebot.types.KeyboardButton("Make a request for document"))
        user_markup.add(telebot.types.KeyboardButton("Show QA"))
        bot.send_message(user_id, "How can I help you?", reply_markup=user_markup)

# Command handler for making a document request
@bot.message_handler(func=lambda message: message.text == 'Make a request for document')
def make_document_request(message):
    user_id = message.from_user.id

    # Fetching frequently asked requests
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
# Function to process selected or another document request
def process_selected_request_or_another(message):
    user_id = message.from_user.id
    selected_option = message.text.strip().lower()

    if selected_option == 'cancel':
        bot.send_message(user_id, "How can I help you?", reply_markup=markup)
    elif selected_option == 'another request':
        bot.send_message(user_id, "Write your request:")
        bot.register_next_step_handler(message, process_another_request)
    else:
        bot.send_message(user_id, f"Your request '{selected_option}' has been received. Please enter your email:")
        bot.register_next_step_handler(message, process_email, request=selected_option)

# Function to process another document request
def process_another_request(message):
    user_id = message.from_user.id
    if message.text.strip().lower() == 'cancel':
        start_handler(message)
    else:
        question = message.text
        bot.send_message(user_id, "Enter your email:")
        bot.register_next_step_handler(message, process_email, request=question)

# Function to process email for document request
def process_email(message, request):
    user_id = message.from_user.id
    email = message.text.strip()
    if email.lower() == 'cancel':
        start_handler(message)
        return
    bot.send_message(user_id, "Please enter your phone number:")
    bot.register_next_step_handler(message, process_phone, request=request, email=email)

# Function to process phone number for document request
def process_phone(message, request, email):
    user_id = message.from_user.id
    phone = message.text.strip()
    if phone.lower() == 'cancel':
        start_handler(message)
        return
    send_email_to_dean_office(request, email, phone)
    bot.send_message(user_id, f"Your request '{request}' with email '{email}' and phone number '{phone}' has been successfully sent!")
    start_handler(message)

# Command handler for canceling the current operation
@bot.message_handler(func=lambda message: message.text.lower() == 'cancel')
def cancel_handler(message):
    start_handler(message)

# Function to send an email to the dean's office
def send_email_to_dean_office(question, email, phone):
    sender_email = "bot email"
    dean_office_email = "dekanat email"

    subject = "New request for documents"
    body = f"Request: {question}\nEmail: {email}\nPhone number: {phone}"

    # get pass (feature)
    sender_password = "password"

    # Sending an email using a password
    yagmail.register(sender_email, sender_password)
    yag = yagmail.SMTP(sender_email)
    yag.send(to=dean_office_email, subject=subject, contents=body)
    yag.close()

    print(f"Your request ({question}) ")

# Command handler for showing QA (Frequently Asked Questions)
@bot.message_handler(func=lambda message: message.text == 'Show QA')
def show_QA_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        # Fetching QA data from the database
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
    else:
        try:
            # Fetching distinct topics from the database
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
# Function to process user's topic choice
def process_user_topic_choice(message):
    user_id = message.from_user.id
    try:
        selected_topic_name = message.text
        if selected_topic_name.lower() == 'cancel':
            start_handler(message)
            return

        # Fetching the topic id based on the selected topic name
        cursor.execute('SELECT topic_id FROM Topics WHERE topic_name=?', (selected_topic_name,))
        selected_topic_id = cursor.fetchone()[0]

        # Fetching questions related to the selected topic
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

# Function to process user's question choice
def process_user_question_choice(message):
    user_id = message.from_user.id
    try:
        selected_question_text = message.text
        if selected_question_text.lower() == 'cancel':
            show_QA_handler(message)
            return

        # Fetching the answer related to the selected question
        cursor.execute(
            'SELECT answer_text FROM Answers WHERE question_id IN (SELECT question_id FROM Questions WHERE question_text=?)',
            (selected_question_text,))
        answer = cursor.fetchone()[0]

        bot.send_message(user_id, f"{answer}")

        start_handler(message)
    except Exception as e:
        print(e)
        bot.send_message(user_id, "Invalid input. Please select a valid question.")

# Command handler for 'Add admin'
@bot.message_handler(func=lambda message: message.text == 'Add admin')
def add_admin_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        users = get_non_admin_users()

        if users:
            markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
            for user in users:
                markup.add(telebot.types.KeyboardButton(str(user)))
            markup.add(telebot.types.KeyboardButton("Cancel"))

            if message.text == "Cancel":
                start_handler(message)
            else:
                bot.send_message(user_id, "Select a user to make him an administrator:", reply_markup=markup)
                bot.register_next_step_handler(message, process_admin_choice)
        else:
            bot.send_message(user_id, "There are no users to add as administrators.")
    else:
        bot.send_message(user_id, "You do not have permission to execute this command.")

# Function to get non-admin users
def get_non_admin_users():
    cursor.execute('SELECT id FROM users WHERE is_admin=0')
    users = cursor.fetchall()
    return [user[0] for user in users]

# Function to process admin choice
def process_admin_choice(message):
    user_id = message.from_user.id
    if message.text == "Cancel":
        start_handler(message)
    else:
        try:
            selected_user_id = int(message.text)
            add_admin(selected_user_id)
            bot.send_message(user_id, f"User with ID {selected_user_id} has been added to administrators.")
        except ValueError:
            bot.send_message(user_id, "Please select the correct user.")
# Command handler for 'Show usersDB'
@bot.message_handler(func=lambda message: message.text == 'Show usersDB')
def show_db_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        # Fetching all users from the 'users' table
        cursor.execute('SELECT * FROM users')
        db_content = cursor.fetchall()
        bot.send_message(user_id, "Database contents:\n" + "\n".join(map(str, db_content)))
    else:
        bot.send_message(user_id, "You do not have permission to execute this command.")

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

# Command handler for 'Change QA'
@bot.message_handler(func=lambda message: message.text == 'Change QA')
def redact_bd_handler(message):
    user_id = message.from_user.id
    if is_user_admin(user_id):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        markup.add(telebot.types.KeyboardButton("Cancel"))

        excel_data = generate_excel_file()
        if excel_data:
            bot.send_document(user_id, excel_data, caption="Edit the file and send it back to update the database.",
                              reply_markup=markup)
            bot.register_next_step_handler(message, process_edited_excel_file)
        else:
            bot.send_message(user_id, "There is no data to create a file.")
    else:
        bot.send_message(user_id, "You do not have permission to execute this command.")

# Command handler for canceling the current operation
@bot.message_handler(func=lambda message: message.text == 'Cancel')
def Cancel_handler(message):
    start_handler(message)

# Function to process an edited Excel file
def process_edited_excel_file(message):
    user_id = message.from_user.id
    if message.text == 'Cancel':
        start_handler(message)
    elif message.document:
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        file_data = bot.download_file(file_info.file_path)

        # Update the database from an edited Excel file
        update_database_from_excel(file_data)

        bot.send_message(user_id, "The database has been successfully updated.")
    else:
        bot.send_message(user_id, "Please send an Excel file to update the database.")

# Function to update the database from an edited Excel file
def update_database_from_excel(file_data):
    try:
        df = pd.read_excel(file_data, engine='openpyxl')

        # Clearing existing data in tables
        cursor.execute('DELETE FROM Topics')
        cursor.execute('DELETE FROM Questions')
        cursor.execute('DELETE FROM Answers')
        conn.commit()

        # Filling the database from DataFrame
        for _, row in df.iterrows():
            topic_name = row['Topic']
            question_text = row['Question']
            answer_text = row['Answer']

            # Add a topic if it doesn't already exist
            cursor.execute('INSERT OR IGNORE INTO Topics (topic_name) VALUES (?)', (topic_name,))
            conn.commit()

            # Get topic id
            cursor.execute('SELECT topic_id FROM Topics WHERE topic_name=?', (topic_name,))
            topic_id = cursor.fetchone()[0]

            # Adding a question
            cursor.execute('INSERT INTO Questions (topic_id, question_text) VALUES (?, ?)', (topic_id, question_text))
            conn.commit()

            # Get the id of the question
            cursor.execute('SELECT question_id FROM Questions WHERE topic_id=? AND question_text=?',
                           (topic_id, question_text))
            question_id = cursor.fetchone()[0]

            # Adding an answer
            cursor.execute('INSERT INTO Answers (question_id, answer_text) VALUES (?, ?)', (question_id, answer_text))
            conn.commit()

        print("The database has been successfully updated.")
    except Exception as e:
        # Error handling, e.g., notifying the administrator of an incorrect file format
        print(f"An error occurred when updating the database from an Excel file: {e}")
       

# Start the bot
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(f"Polling error: {e}")
        time.sleep(10)
