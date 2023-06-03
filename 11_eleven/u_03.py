# импортирование файла
# из modul_1.py
import modul_1
print(modul_1.max1(5, 9))


# импорт на прямую
from modul_1 import max1
print(max1(3, 4))

# импорт на прямую всех функций 
from modul_1 import *
print(max1(6, 4))

# короткое название модуля
import modul_1 as m1
print(m1.max1(6,11))