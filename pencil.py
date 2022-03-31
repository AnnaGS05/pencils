#  Пример объектно-ориентированного программирония (ООП)

from settings import *  # Настройки выносим в отдельный файл.

x = 10
y = 10


def setup(amount):  # Параметр amount - кол-во карандашей.
    global x, y  # Речь идет о переменных в 5 и 6 строках. Они видны во всех функциях модуля.
    y = CANVAS_HEIGHT / 2 - (PENCIL_MAX_LENGTH * CM + PENCIL_CONE) / 2
    pencil_box_width = amount * (PENCIL_WIDTH + GAPE) - GAPE  # Локальная переменная, действует только внутри данной функции.
    x = (CANVAS_WIDTH - pencil_box_width) / 2


def get_quarters():
    return x + PENCIL_WIDTH / 4, x + PENCIL_WIDTH / 4 * 3


class Pencil:  # Класс - описание объекта (в данном случае карандаша)

    def __init__(self, canvas,  color, length, sharpness):  # Конструктор, создает новый экземпляр класса
        self.canvas = canvas
        self.color = color
        self.length = length
        self.sharpness = sharpness

    def get_bottom_right(self):
        return x + PENCIL_WIDTH, y + self.length * CM  # Возвращает координаты нижнего правого угла.

    def get_small_cone(self):
        x1 = x + PENCIL_WIDTH / 4
        x2 = x + PENCIL_WIDTH / 4 * 3
        y1 = y + self.length * CM + PENCIL_CONE / 2
        return x1, y1, x2, y1

    def get_pencil_tip(self):
        x_tip = x + PENCIL_WIDTH / 2
        y_tip = y + self.length * CM + PENCIL_CONE
        return x_tip, y_tip

    def draw(self):
        global x, y
        x_br, y_br = self.get_bottom_right()  # Кортеж расскладываем на переменные.
        x_q1, x_q2 = get_quarters()  # Узкй прямоугольник.
        x_tip, y_tip = self.get_pencil_tip()
        x_sc1, y_sc1, x_sc2, y_sc2 = self.get_small_cone()
        print(f'Цвет: {self.color}; длина: {self.length} см; {"острый" if self.sharpness else "тупой"}.')
        self.canvas.create_rectangle(x, y, x_br, y_br, fill=self.color)
        self.canvas.create_rectangle(x_q1, y, x_q2, y_br)
        self.canvas.create_polygon(x, y_br, x_tip, y_tip, x_br, y_br, fill="white", outline="black")
        if self.sharpness:
            self.canvas.create_polygon(x_sc1, y_sc1, x_sc2, y_sc2, x_tip, y_tip, fill=self.color, outline="black")
        else:
            self.canvas.create_rectangle(x_sc1, y_sc1 + 3,
                                    x_sc2, y_tip + 3, fill="white",
                                    outline="white")
            self.canvas.create_polygon(x_sc1, y_sc2,
                                  x + PENCIL_WIDTH / 8 * 3, y + self.length * CM + PENCIL_CONE - 20,
                                  x + PENCIL_WIDTH / 8 * 5, y + self.length * CM + PENCIL_CONE - 20,
                                  x_sc2, y_sc2, fill=self.color,
                                  outline="black")
        x += PENCIL_WIDTH + GAPE

