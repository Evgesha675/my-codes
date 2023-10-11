import telebot
from telebot import types

# Инициализация бота
bot=telebot.TeleBot('')

# Создаем клавиатуру с 10 кнопками
markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button_stats = []
# Создаем список кнопок
button1 = types.KeyboardButton("Кнопка 1")
button2 = types.KeyboardButton("Кнопка 2")
button3 = types.KeyboardButton("Кнопка 3")
button4 = types.KeyboardButton("Кнопка 4")
button5 = types.KeyboardButton("Кнопка 5")
button6 = types.KeyboardButton("Кнопка 6")
button7 = types.KeyboardButton("Кнопка 7")
button8 = types.KeyboardButton("Кнопка 8")
button9 = types.KeyboardButton("Кнопка 9")
restart_bot = types.KeyboardButton("Старт")

# Добавляем кнопки к клавиатуре
markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, restart_bot)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработчики кнопок
@bot.message_handler(func=lambda message: message.text == "Кнопка 1")
def button1_handler(message):
    # Здесь можно добавить логику для кнопки 1, например, отправку документа
    bot.send_document(message.chat.id, open("C:/Users/Vitaliy/Desktop/png и нужные файлы/1988776886_preview_Слой 1.png", "rb"))


@bot.message_handler(func=lambda message: message.text == "Кнопка 2")
def button2_handler(message):
    # Здесь можно добавить логику для кнопки 2
     bot.send_document(message.chat.id, open("C:/Users/Vitaliy/Desktop/png и нужные файлы/1988776886_preview_Слой 2.png", "rb"))
@bot.message_handler(func=lambda message: message.text == "Кнопка 3")
def button3_handler(message):
    # Отправка аудиофайла MP3
    audio_path = "C:/Users/Vitaliy/Desktop/png и нужные файлы/Camellia - Light It Up (mp3cut.net).mp3"
    with open(audio_path, "rb") as audio:
        bot.send_audio(message.chat.id, audio)
# Обработчик кнопки "Перезапустить бота"
@bot.message_handler(func=lambda message: message.text == "Старт")
def restart_handler(message):
    start(message) 


# Функция для записи события нажатия кнопки в массив
def record_button_stats(button_text):
    button_stats.append(button_text)
    print("Записано нажатие кнопки:", button_text)
# Обработчик команды /stats
@bot.message_handler(commands=['stats'])
def show_button_stats(message):
    # Преобразуем массив button_stats в строку для вывода
    stats_str = "\n".join(button_stats)
    
    if stats_str:
        bot.send_message(message.chat.id, "Статистика нажатия кнопок:\n" + stats_str)
    else:
        bot.send_message(message.chat.id, "Статистика нажатия кнопок пуста.")

# Обработчик нажатия кнопки для вывода статистики
@bot.message_handler(func=lambda message: message.text == "Показать статистику")
def show_stats_button_handler(message):
    show_button_stats(message)  # Вызываем обработчик команды /stats





    
# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
