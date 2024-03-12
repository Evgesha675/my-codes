import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import executor

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '6378551854:AAGBtcq3xKjIduZym771lElsImrlJ08L64c'

# Уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Хендлер на команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который готов общаться с вами.")

# Функция для старта бота
async def on_startup(dp):
    logging.info("Бот запущен!")

# Функция для остановки бота
async def on_shutdown(dp):
    logging.info("Бот остановлен!")

if __name__ == '__main__':
    from aiogram import executor
    from aiogram.types import BotCommand

    # Добавление команды /start
    bot_commands = [
        BotCommand(command="/start", description="Начать общение с ботом"),
    ]
    dp.bot.set_my_commands(bot_commands)

    # Запуск бота
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
