#!/usr/bin/python3
# ДАННЫЙ ПРИМЕР ВЫВОДИТ НАПРАВЛЕНИЯ ДЖОЙСТИКА В ГРАДУСАХ:

from time import sleep
from math import atan2, pi

# Подключаем библиотеку для работы с джойстиком I2C-flash.
from pyiArduinoI2Cjoystick import *

# Объявляем объект joy для работы с библиотекой, указывая адрес модуля на шине.
j = pyiArduinoI2Cjoystick(0x09)


print("Выводим положение джойстика в полярной системе координат.")
print("Для выхода нажмите <ctrl+c>")

while True:

    # Получаем текущие координаты
    x, y = j.x, j.y

    # Вычисляем радианы
    rad = atan2(y,x)
    deg = rad * (180 / pi)

    if deg < 0:
        deg = deg + 360

    # Выводим градусы
    print(round(deg))

    sleep(.1)
