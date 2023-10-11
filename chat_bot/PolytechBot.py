import sqlite3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создаем таблицу для хранения информации о пользователях и администраторах
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        is_admin INTEGER
    )
''')
conn.commit()

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    is_admin = is_user_admin(user_id)
    if is_admin:
        keyboard = [[("Добавить нового администратора", "add_admin")], [("Показать БД", "show_db")]]
    else:
        keyboard = []
    
    reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
    update.message.reply_text("Привет! Я ваш бот.", reply_markup=reply_markup)

# Функция для проверки, является ли пользователь администратором
def is_user_admin(user_id: int) -> bool:
    cursor.execute('SELECT * FROM users WHERE id=? AND is_admin=1', (user_id,))
    return cursor.fetchone() is not None

# Функция для добавления нового администратора в базу данных
def add_admin(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    cursor.execute('INSERT INTO users (id, is_admin) VALUES (?, 1)', (user_id,))
    conn.commit()
    update.message.reply_text(f"Пользователь с ID {user_id} добавлен в администраторы.")

# Функция для показа базы данных
def show_db(update: Update, context: CallbackContext) -> None:
    cursor.execute('SELECT * FROM users')
    db_content = cursor.fetchall()
    update.message.reply_text("Содержимое базы данных:\n" + "\n".join(map(str, db_content)))

def main() -> None:
    # Ваш токен бота
    token = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'
    updater = Updater(token)

    # Добавляем обработчики команд
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^Добавить нового администратора$'), add_admin))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^Показать БД$'), show_db))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
