# Коробка с карандашами: приложение с оконом интерфейсом (GUI).

from tkinter import *  # Используем возможности модуля tkinter.

from pencil import Pencil, setup
from settings import *  # Настройки выносим в отдельный файл.

window = Tk()  # Создаем окно.
window.title(TITLE)
# label = Label(text="Привет.")  # Создаем метку.
# label.pack()  # Упаковываем метку.
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)  # Холст для рисования.
canvas.pack()

pencils =  [  # Список кортежей с описанием карандашей.
    ("red", 10, True),
    ("blue", 12, True),
    ("blue", 18, True),
    ("green", 8, False),
    ("gray", 7, False),
    ("gray", 2, False)

]

def draw_pencils(name):  # Объявление функции (definition). Параметр (name).
    print(name)
    pencils_filtered = list(filter(lambda p: PENCIL_MIN_LENGTH <= p[1] <= PENCIL_MAX_LENGTH, pencils))
    setup(len(pencils_filtered))
    for pencil in pencils_filtered:  # Для каждого карандаша в наборе.
        color, length, sharpness = pencil  # Извлекаем переменные из кортежа.
        pencil = Pencil(canvas, color, length, sharpness)
        pencil.draw()

    mainloop()  # Запускаем окно.

if __name__ == '__main__':
    draw_pencils('Коробка с карандашами')  # Вызов функции.
