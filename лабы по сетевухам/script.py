import json
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

def load_schedule():
    with open('schedule.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def format_schedule(day, day_schedule):
    formatted_schedule = f"Расписание на {day, current_week}:\n"
    for time, activities in day_schedule.items():
        formatted_schedule += f"{time} - {', '.join(activities)}\n"
    return formatted_schedule

def get_weekday_schedule(day):
    schedule = load_schedule()
    requested_day = f"{day}{current_week}"
    print("Requested day:", requested_day)  # Добавляем вывод запрашиваемого дня недели для отладки
    return schedule.get(requested_day, "На этот день расписания нет.")

def current_week():

    today = datetime.datetime.now()
    # Получаем начало учебного года
    start_of_school_year = datetime.datetime(today.year, 9, 1)
    # Вычисляем разницу в днях между текущей датой и началом учебного года
    days_since_start = (today - start_of_school_year).days
    # Определяем, сколько полных недель прошло с начала учебного года
    weeks_since_start = days_since_start // 7
    # Если количество недель четное, то это четная неделя, иначе - нечетная
    if weeks_since_start % 2 == 0:
        return 2  # Четная неделя
    else:
        return 1  # Нечетная неделя

def handler(event, context):
    text = 'Спроси расписание'
    current_week_number = current_week()
    
    if 'request' in event and 'original_utterance' in event['request']:
        utterance = event['request']['original_utterance'].lower()
        if 'сегодня' in utterance:
            today = datetime.datetime.now().strftime("%A")
            print("Сегодня:", today)  # Добавляем вывод текущего дня недели для отладки
            if datetime.datetime.now().weekday() == 6:  # Проверка, является ли сегодня воскресеньем
                text = "Сегодня воскресенье, занятий нет. Идти не нужно."
            else:
                text = f"Расписание на сегодня ({today}): {get_weekday_schedule(today, current_week_number)}"
        elif 'завтра' in utterance:
            tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
            if tomorrow.weekday() == 6:  # Проверка, является ли завтра воскресеньем
                text = "Завтра воскресенье, занятий нет. Идти не нужно."
            else:
                tomorrow_day = tomorrow.strftime("%A")
                text = f"Расписание на завтра ({tomorrow_day}): {get_weekday_schedule(tomorrow_day, current_week_number)}"
    
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': False
        }
    }
