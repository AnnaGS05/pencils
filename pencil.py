#  Пример объектно-ориентированного программирония (ООП)

from settings import *  # Настройки выносим в отдельный файл.

x = 10
y = 10


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

    def draw(self):
        global x, y
        x_br, y_br = self.get_bottom_right()  # Кортеж расскладываем на переменные.
        x_q1, x_q2 = get_quarters()
        print(f'Цвет: {self.color}; длина: {self.length} см; {"острый" if self.sharpness else "тупой"}.')
        self.canvas.create_rectangle(x, y, x_br, y_br, fill=self.color)
        self.canvas.create_rectangle(x_q1, y, x_q2, y_br)
        self.canvas.create_polygon(x, y + self.length * CM, x + PENCIL_WIDTH / 2, y + self.length * CM + PENCIL_CONE,
                              x + PENCIL_WIDTH, y + self.length * CM, fill="white", outline="black")
        if self.sharpness:
            self.canvas.create_polygon(x + PENCIL_WIDTH / 4, y + self.length * CM + PENCIL_CONE / 2,
                                  x + PENCIL_WIDTH / 2, y + self.length * CM + PENCIL_CONE,
                                  x + PENCIL_WIDTH / 4 * 3, y + self.length * CM + PENCIL_CONE / 2, fill=self.color,
                                  outline="black")
        else:
            self.canvas.create_rectangle(x + PENCIL_WIDTH / 4, y + self.length * CM + PENCIL_CONE / 2 + 3,
                                    x + PENCIL_WIDTH / 4 * 3, y + self.length * CM + PENCIL_CONE, fill="white",
                                    outline="white")
            self.canvas.create_polygon(x + PENCIL_WIDTH / 4, y + self.length * CM + PENCIL_CONE / 2,
                                  x + PENCIL_WIDTH / 8 * 3, y + self.length * CM + PENCIL_CONE - 20,
                                  x + PENCIL_WIDTH / 8 * 5, y + self.length * CM + PENCIL_CONE - 20,
                                  x + PENCIL_WIDTH / 4 * 3, y + self.length * CM + PENCIL_CONE / 2, fill=self.color,
                                  outline="black")
        x += PENCIL_WIDTH + GAPE

