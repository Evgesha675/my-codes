import requests
import json


url = "https://bki.forlabs.ru/lm-vendor/repositories/sched/get_schedule"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json, text/plain, */*",
    
    "X-Xsrf-Token": "eyJpdiI6ImZlRk1vOTY0NjBLUHRJcjdVQytqalE9PSIsInZhbHVlIjoicnI3aXlvUFR0c05jOWNESmdFaVptTzQ1ZlFzNjEyVGl4SE1rMG45REM5QUtsWGJQMzhJbVYzYTFUWTJ2cHFmYURHN1NHNzQrdnFwdEY4ZTh5WXFIbnpiMFNcL3BkOGNrOXNQQ0F5VWxOeE56UDRKdlwveTRLVDhYcHlneFFsc2RSTSIsIm1hYyI6IjIyMTQzMzc3OTU1OGQ0NGY4NzFlNDQ0ODAxMTFiNzdjNjdlYmYwMWQzODMyZmY1YTZjMGZkY2I1NzI3YjVlNTkifQ==",
    "Cookie": "remember_lm_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjN5V3RsdnBZZXdUV21TK283czRGZVE9PSIsInZhbHVlIjoiUlZ1Zlp1VUpuSnVCQVdMdytcLzZTc2pKRDRCQ3JWQ2NhSmNjbW9LTENnNmhwMWxEUVdDU3ZJVmM3TnVcLzVSMzhETUsrSEZ0V0dLNTRHRDh6ZWZ5cFVvalo3bUNzMnlHcGt0TVR1Ym1YV1dkWWFUYThqbEQySkJvR1ZEMEhpQ0VWbkJMUGpwaWFWb0NlaUVtVUJnb3FjRVdIYmI2aUhHRVNEcHJ1XC9wRzEwUEh2YVZMNXJRY2JoazlubVhFRlNkVU5nOGlPekNUMmJaRUFwUmFXY2M4UjJkOGZwRnd2SDFTRk1MclNUSisxZWRsaz0iLCJtYWMiOiI1MzY1ODliOGRjNGIwNzIzZGRhYTA2OTM4Y2JkNTBlYTcwZWY3ZGE0NTY1ODAzZTNkNmMyMjUwZTU3ZjU5NWYyIn0%3D; XSRF-TOKEN=eyJpdiI6ImZlRk1vOTY0NjBLUHRJcjdVQytqalE9PSIsInZhbHVlIjoicnI3aXlvUFR0c05jOWNESmdFaVptTzQ1ZlFzNjEyVGl4SE1rMG45REM5QUtsWGJQMzhJbVYzYTFUWTJ2cHFmYURHN1NHNzQrdnFwdEY4ZTh5WXFIbnpiMFNcL3BkOGNrOXNQQ0F5VWxOeE56UDRKdlwveTRLVDhYcHlneFFsc2RSTSIsIm1hYyI6IjIyMTQzMzc3OTU1OGQ0NGY4NzFlNDQ0ODAxMTFiNzdjNjdlYmYwMWQzODMyZmY1YTZjMGZkY2I1NzI3YjVlNTkifQ%3D%3D; forlabs_session=eyJpdiI6InpRZUNpZVVxVzB4Y2VjeW1jNmVqREE9PSIsInZhbHVlIjoiZHRYZHlmRXh6eFBDelNvM2wyUkFocGg3NGViWmkzZ3FqeDNNYWhQZSs5Tk5ONllOUFpwS0NZbkttRitydnFReXNjeW85Z0FobDIwNHlJczdpQ3hRWTZZUVwvalJ2OEwxYVkyNmJTcVBveEpEZWNOaHN6XC9NT1FSeldsTFM4SjVIViIsIm1hYyI6ImJhNzdhYTRmODhkMzFlYmYwOTJmZWE3ODFkZDYwNWMzNjNmY2MyZDgxMDk0NTU0YWY3OWU2MGVlYzIwY2NjN2UifQ%3D%3D"

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
