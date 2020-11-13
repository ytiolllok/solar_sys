# coding: utf-8
# license: GPLv3

import pygame as pg

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""

colordict = {'red':  (232, 48, 48),
             'orange': (236, 106, 16),
             'blue': (50, 27, 249),
             'green': (104, 229, 57),
             'yellow': (234, 243, 53),
             'white': (255, 255, 255),
             'gray':  (103, 131, 121),
             }


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.2 * min(window_height, window_width) / max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Параметры:
    **x** — x-координата модели.
    """

    return int(x * scale_factor) + window_width // 2


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.
    Параметры:
    **y** — y-координата модели.
    """
    return -int(y * scale_factor) + window_height // 2


if __name__ == "__main__":
    print("This module is not for direct call!")


class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def update(self, figures, ui):
        self.screen.fill((0, 0, 0))
        for figure in figures:
            figure.draw(self.screen)

        ui.blit()
        ui.update()
        pg.display.update()


class DrawableObject:
    def __init__(self, obj):
        self.obj = obj

    def draw(self, surface):
        pg.draw.circle(surface, self.obj.color, (int(scale_x(self.obj.x)), int(scale_y(self.obj.y))), int(self.obj.R))
