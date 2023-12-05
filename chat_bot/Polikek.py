import smtplib
import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="telegram.ext.conversationhandler")
# States
FEEDBACK_QUESTION, FEEDBACK_EMAIL = range(2)

# Database setup
conn = sqlite3.connect('questions.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question_text TEXT,
        user_email TEXT
    )
''')

conn.commit()

# Telegram Bot setup
TOKEN = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Command handler for /start
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("List of Questions", callback_data='list')],
        [InlineKeyboardButton("Feedback", callback_data='feedback')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Hello, what do you need?", reply_markup=reply_markup)

# Callback query handler
def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'list':
        # Fetch and display a list of questions (for now, it's an empty list)
        questions = get_questions()
        response = "List of Questions:\n" + "\n".join(questions)
        query.edit_message_text(text=response)

    elif query.data == 'feedback':
        # Ask the user for a question
        query.edit_message_text(text="Please enter your question:")
        return FEEDBACK_QUESTION

# Message handler for feedback question
def feedback_question(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    context.user_data['feedback'] = {'user_id': user_id, 'question_text': update.message.text}

    # Ask for the user's email
    update.message.reply_text("Please enter your email:")
    return FEEDBACK_EMAIL

# Message handler for feedback email
def feedback_email(update: Update, context: CallbackContext):
    user_id = context.user_data['feedback']['user_id']
    question_text = context.user_data['feedback']['question_text']
    email = update.message.text

    # Save the question and email in the database
    save_feedback(user_id, question_text, email)

    # Send the question and email to a specific email address
    send_feedback_email(question_text, email)

    update.message.reply_text("Thank you! Your feedback has been submitted.")
    del context.user_data['feedback']

    return ConversationHandler.END

# Helper function to get a list of questions
def get_questions():
    cursor.execute("SELECT question_text FROM questions")
    questions = cursor.fetchall()
    return [q[0] for q in questions]

# Helper function to save a question and email in the database
def save_feedback(user_id, question_text, email):
    cursor.execute("INSERT INTO questions (question_text, user_email) VALUES (?, ?)", (question_text, email))
    conn.commit()

# Helper function to send feedback to a specific email address
def send_feedback_email(question_text, email):
    # Implement email sending logic here
    # Example using smtplib:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('anatolevicanatolij@gmail.com', 'evgesha675124')
        server.sendmail('anatolevicanatolij@gmail.com', 'tetenkinevgenij@gmail.com', f'Subject: Feedback\n\nQuestion: {question_text}\nEmail: {email}')

# Conversation handler
feedback_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(button_click)],
    states={
        FEEDBACK_QUESTION: [MessageHandler(Filters.text & ~Filters.command, feedback_question)],
        FEEDBACK_EMAIL: [MessageHandler(Filters.regex(r'[^/].+@[^/].+\.[^/].+'), feedback_email)],
    },
    fallbacks=[]
)



# Handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

dispatcher.add_handler(feedback_handler)

# Start the Bot
updater.start_polling()
updater.idle()
