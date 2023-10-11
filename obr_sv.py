from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'

# ID двух аккаунтов, к которым бот будет подключен
ACCOUNT1_ID = '633294626'


def start(update: Update, _: CallbackContext) -> None:
    """Отправляет id пользователя, который запустил бота."""
    user_id = update.message.from_user.id
    update.message.reply_text(f'Ваш ID: {user_id}')

def forward_message(update: Update, _: CallbackContext) -> None:
    """Пересылает сообщение от пользователя на указанные аккаунты."""
    user_id = update.message.from_user.id
    message_text = update.message.text

    # Отправка сообщения на аккаунт1
    # replace 'ACCOUNT1_ID' with the actual ID of the first account
    context.bot.send_message(chat_id=ACCOUNT1_ID, text=f'Пользователь {user_id}: {message_text}')

    # Отправка сообщения на аккаунт2
    # replace 'ACCOUNT2_ID' with the actual ID of the second account
    context.bot.send_message(chat_id=ACCOUNT2_ID, text=f'Пользователь {user_id}: {message_text}')

def main() -> None:
    """Запускает бота."""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Обработка команды /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Обработка всех входящих сообщений (пересылка)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
