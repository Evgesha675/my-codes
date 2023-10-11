import pyautogui
import time
from PIL import Image, ImageDraw

# Разрешение первого монитора
monitor1_width = 1280
monitor1_height = 1024

# Разрешение второго монитора
monitor2_width = 1920
monitor2_height = 1080

# Цвет и размер точки
dot_color = (255, 0, 0)  # Красный цвет (RGB)
dot_radius = 2  # Размер точки

# Создаем бесконечный цикл
while True:
    # Получаем текущее положение курсора на первом мониторе
    x1, y1 = pyautogui.position()

    # Конвертируем положение курсора на первом мониторе в положение на втором мониторе
    x2 = int((x1 / monitor1_width) * monitor2_width)
    y2 = int((y1 / monitor1_height) * monitor2_height)

    # Создаем изображение экрана второго монитора
    screenshot = pyautogui.screenshot()
    draw = ImageDraw.Draw(screenshot)

    # Рисуем точку на изображении
    draw.ellipse([x2 - dot_radius, y2 - dot_radius, x2 + dot_radius, y2 + dot_radius], fill=dot_color)

    # Отображаем обновленное изображение
    screenshot.show()

    # Задержка между обновлениями
    time.sleep(0.01)
