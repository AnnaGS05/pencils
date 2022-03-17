# Коробка с карандашами: приложение с оконом интерфейсом (GUI).

from tkinter import *  # Используем возможности модуля tkinter.
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

x = 10
y = 10


def draw_pencil(color, length, is_sharp):  # Функция принимает три параментра.
    global x, y  # Глобальнве переменные, смотреть строки 19, 20
    print(f'Цвет: {color}; длина: {length} см; {"острый" if is_sharp else "тупой"}.')
    canvas.create_rectangle(x, y, x + PENCIL_WIDTH, y + length * CM, fill=color)
    canvas.create_rectangle(x + PENCIL_WIDTH/4, y, x + PENCIL_WIDTH/4*3, y + length * CM)
    canvas.create_polygon(x, y + length * CM, x + PENCIL_WIDTH/2, y + length * CM + PENCIL_CONE,
                          x + PENCIL_WIDTH,  y + length * CM, fill="white", outline="black")
    if is_sharp:
        canvas.create_polygon(x + PENCIL_WIDTH/4, y + length * CM + PENCIL_CONE/2,
                              x + PENCIL_WIDTH/2, y + length * CM + PENCIL_CONE,
                              x + PENCIL_WIDTH/4*3, y + length * CM + PENCIL_CONE/2, fill=color, outline="black")
    else:
        canvas.create_rectangle(x + PENCIL_WIDTH / 4, y + length * CM + PENCIL_CONE / 2 + 3,
                                x + PENCIL_WIDTH / 4 * 3, y + length * CM + PENCIL_CONE, fill="white", outline="white")
        canvas.create_polygon(x + PENCIL_WIDTH/4, y + length * CM + PENCIL_CONE/2,
                              x + PENCIL_WIDTH/8*3,y + length * CM + PENCIL_CONE - 20,
                              x + PENCIL_WIDTH/8*5,y + length * CM + PENCIL_CONE - 20,
                              x + PENCIL_WIDTH / 4 * 3, y + length * CM + PENCIL_CONE/2, fill=color, outline="black")
    x += PENCIL_WIDTH + GAPE

def draw_pencils(name):  # Объявление функции (definition). Параметр (name).
    print(name)
    pencils_filtered = list(filter(lambda p: p[1] >= 5 and p[1] <= 15, pencils))
    print(len(pencils_filtered))
    for pencil in pencils_filtered:  # Для каждого карандаша в наборе.
        color, length, sharpness = pencil  # Извлекаем переменные из кортежа.
    #    if length > 15:
    #        print("Слишком длинный карандаш.")
    #        continue
    #    if length < 5:
    #        print("Слишком короткий карандаш.")
    #        continue
        draw_pencil(color, length, sharpness)  # Вызываем функцию с 3 аргументами.

    mainloop()  # Запускаем окно.

if __name__ == '__main__':
    draw_pencils('Коробка с карандашами')  # Вызов функции.
