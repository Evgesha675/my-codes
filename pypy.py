import requests
from datetime import datetime

# Определение верхней недели
current_day_of_week = datetime.now().isocalendar()[2]
upperweek = 1 if current_day_of_week % 2 == 1 else 2

url = "https://bki.forlabs.ru/lm-vendor/repositories/sched/get_schedule"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json, text/plain, */*",
    "X-Xsrf-Token": "eyJpdiI6IkdkOEhucnBBbnVCajlBZTY4WWZKWWc9PSIsInZhbHVlIjoiZXJoZ0FQUUJjWWVnRGlrK3huZWVtaWFxblNpVEQ0blwvVnhVK0FVcmNXbFU3UmcrZ3JGNCtLMGZ5SThxb1hMcHBFa2VWSHZkWjh0WVhrcVdOQ0tDUGx5RFljMWN5Y2pjNDRGbXgwQW01UmFsUEVrdHA0NXBURElTTVFlMjZoWG9sIiwibWFjIjoiNGQ2OTU3NjM2YjExMDdkNzA1M2IzNjA4NmE5NTVmOWVkYjY5NmZjNmVlYTA5ZTc2ZmQ3N2NhN2IyNTBiZTMwMyJ9",
    "Cookie": "XSRF-TOKEN=eyJpdiI6IkdkOEhucnBBbnVCajlBZTY4WWZKWWc9PSIsInZhbHVlIjoiZXJoZ0FQUUJjWWVnRGlrK3huZWVtaWFxblNpVEQ0blwvVnhVK0FVcmNXbFU3UmcrZ3JGNCtLMGZ5SThxb1hMcHBFa2VWSHZkWjh0WVhrcVdOQ0tDUGx5RFljMWN5Y2pjNDRGbXgwQW01UmFsUEVrdHA0NXBURElTTVFlMjZoWG9sIiwibWFjIjoiNGQ2OTU3NjM2YjExMDdkNzA1M2IzNjA4NmE5NTVmOWVkYjY5NmZjNmVlYTA5ZTc2ZmQ3N2NhN2IyNTBiZTMwMyJ9 XSRF-TOKEN; forlabs_session= eyJpdiI6ImRJMHlYZ2RlbnZYQWhOT1g0TUhCQmc9PSIsInZhbHVlIjoickN3MjFQVmdZQzUxYXJMKzBxWXdEejNNbU14TUtJQ05qTkdEMEFNbjJjU04xZXV1R0VDY01DRjF5dmtvVmJhOVwvb0hxS3JMNEhZOFVWdDFjSGxjeDNXYlc4UzRHY3RaYXFoVU5JVEhoeDh5ZkY1ek4xU21MS2tWc24xaUE2WGlyIiwibWFjIjoiNDY1MTNkOWVjN2U2Y2MwNmJiMzBmZmE4Mzc4ZjBiYjQ1Yzk3NGYzNzQ4NzFhODkzZjRjMjA1M2NiYzA1ZWU1ZiJ9"
}

data = {}  # Вставьте необходимые данные запроса

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    json_data = response.json()
    entries = json_data.get('entries', [])
    
    # Создаем HTML таблицу
    html_table = "<table border='1'><tr><th>Time</th><th>Lesson</th><th>Type</th><th>Lecturer</th><th>Room</th></tr>"
    
    for entry in entries:
        start_time = entry.get('positions', [])[0].get('start')
        end_time = entry.get('positions', [])[0].get('end')
        lesson_name = entry.get('lesson_name')
        lesson_type = entry.get('type')
        lecturer_name = entry.get('lecturer_name')
        room_name = entry.get('room_name')
        
        html_table += f"<tr><td>{start_time} - {end_time}</td><td>{lesson_name}</td><td>{lesson_type}</td><td>{lecturer_name}</td><td>{room_name}</td></tr>"
    
    html_table += "</table>"
    
    # Выводим таблицу
    print(html_table)
else:
    print(f"Произошла ошибка: {response.status_code}")
