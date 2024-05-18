import requests
import json


url = "https://bki.forlabs.ru/lm-vendor/repositories/sched/get_schedule"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json, text/plain, */*",
    "X-Xsrf-Token": "eyJpdiI6Ik04UHBxNVR4dWFIRnhrQzNZMDRCVkE9PSIsInZhbHVlIjoiRmR2MlVwcWF5c3Y5UzZ4ZFlGQ3oxc2Z6MW1tbFMzeHltVkJNejFmd3lrd1wvUDc3SzNIeGFIMWJPUEgzUUxlUFEwdTFkRG12U3F5enhEdkpYdW9yOUlCcjBacG42VzZta1FaNGtRSVpJRFpIRmdCMzZrTXE5b1NGbk56U1BaQkh4IiwibWFjIjoiODc0NWFmNjkyMTA2ZDIwZWRhNTc4NTY3ODBiNjBhY2ViZjJjMTBjMDU3YzU1NDgzZjQ1N2M2MGIxNjVmOWY5OCJ9",
    "Cookie": "XSRF-TOKEN=eyJpdiI6Ik04UHBxNVR4dWFIRnhrQzNZMDRCVkE9PSIsInZhbHVlIjoiRmR2MlVwcWF5c3Y5UzZ4ZFlGQ3oxc2Z6MW1tbFMzeHltVkJNejFmd3lrd1wvUDc3SzNIeGFIMWJPUEgzUUxlUFEwdTFkRG12U3F5enhEdkpYdW9yOUlCcjBacG42VzZta1FaNGtRSVpJRFpIRmdCMzZrTXE5b1NGbk56U1BaQkh4IiwibWFjIjoiODc0NWFmNjkyMTA2ZDIwZWRhNTc4NTY3ODBiNjBhY2ViZjJjMTBjMDU3YzU1NDgzZjQ1N2M2MGIxNjVmOWY5OCJ9; forlabs_session=eyJpdiI6IlcwUVA2Zll6amlrNTBqVFlmZlh2QVE9PSIsInZhbHVlIjoiaXY3QzUzcHNRV1hBT0RvTTlsWWJXWkJtRGpDOWk4U3FDWDRFSWNBRit6ZzVKeHk1UEp2UTlYMEY5UHFEdEU0dWE4eGJjWmRvWW9YWVQ3eHBERDFvbnBaTXZJZ1pNVGRpTFVIWCt3dHhwNUNheERJcWt0NkJpMWpwKzdcL21QNzRkIiwibWFjIjoiNjBlOGFmYzYyMGI1MjY0NjNhZTEyM2Q0ZjY2YzM4OGU4NGFhNGJhMDg1MTVkMjJjMzVhMzc2Y2M2MWVmZGU2MSJ9"
    

}
data = {}  # Вставьте необходимые данные запроса

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    json_data = response.json()
    entries = json_data.get('entries', [])
    
    schedule = []
    for entry in entries:
        day = entry.get('day')
        position = entry.get('position')
        room_name = entry.get('room_name')
        lecturer_name = entry.get('lecturer_name')
        study_name = entry.get('study_name')
        
        schedule.append({
            "Day": day,
            "Position": position,
            "Room": room_name,
            "Lecturer": lecturer_name,
            "Study_name": study_name
        })
    
    # Запись полученных данных в файл JSON
    with open("schedule.json", "w", encoding="utf-8") as file:
        json.dump(schedule, file, ensure_ascii=False, indent=4)
    
    print("Данные успешно записаны в файл 'schedule.json'")
    
else:
    print(f"Произошла ошибка: {response.status_code}")
