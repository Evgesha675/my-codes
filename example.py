import tkinter as tk
from tkinter import messagebox

def show_age():
    age = age_entry.get()
    if age.isdigit():
        messagebox.showinfo("Ваш возраст", f"Ваш возраст: {age}")
    else:
        messagebox.showerror("Ошибка", "Введите корректный возраст!")

# Создание основного окна
root = tk.Tk()
root.title("Введите ваш возраст")

# Метка и поле для ввода возраста
tk.Label(root, text="Введите ваш возраст:").pack(pady=10)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

# Кнопка подтверждения
ok_button = tk.Button(root, text="OK", command=show_age)
ok_button.pack(pady=10)

# Запуск основного цикла обработки событий
root.mainloop()
