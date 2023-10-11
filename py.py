from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# States for the ConversationHandler
BUTTON_TYPE, FILE_UPLOAD, LINK_INPUT = range(3)

# Dictionary to store admin usernames (for demonstration purposes)
admin_usernames = {'admin_username1', 'admin_username2'}

# Command handlers
def start(update: Update, _: CallbackContext) -> int:
    # Check if user is admin
    if update.message.from_user.username in admin_usernames:
        update.message.reply_text("Welcome, Admin! Use /createbutton to create buttons.")
        return BUTTON_TYPE
    else:
        update.message.reply_text("You are not authorized to use this bot.")
        return ConversationHandler.END

def button_type(update: Update, _: CallbackContext) -> int:
    keyboard = [[InlineKeyboardButton("File Upload", callback_data='file_upload'),
                 InlineKeyboardButton("Link Input", callback_data='link_input')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose a button type:', reply_markup=reply_markup)
    return BUTTON_TYPE

def file_upload(update: Update, _: CallbackContext) -> int:
    update.message.reply_text('Please upload a file.')
    return FILE_UPLOAD

def handle_file_upload(update: Update, _: CallbackContext) -> int:
    file = update.message.document.get_file()
    file.download('files/' + file.file_path.split('/')[-1])
    update.message.reply_text('File uploaded successfully!')
    return ConversationHandler.END

def link_input(update: Update, _: CallbackContext) -> int:
    update.message.reply_text('Please send the link.')
    return LINK_INPUT

def handle_link_input(update: Update, _: CallbackContext) -> int:
    link = update.message.text
    update.message.reply_text('Link added successfully!')
    return ConversationHandler.END

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("YOUR_BOT_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            BUTTON_TYPE: [CallbackQueryHandler(button_type, pattern='^(file_upload|link_input)$')],
            FILE_UPLOAD: [MessageHandler(None, handle_file_upload, pass_user_data=True)],
            LINK_INPUT: [MessageHandler(None, handle_link_input, pass_user_data=True)],
        },
        fallbacks=[],
    )

    dispatcher.add_handler(conversation_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
