# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random
n = int(input('количество элементов первого множества: '))
m = int(input('количество элементов второго множества: '))
list_1 = [random.randint(1,10) for i in range(1, n+1) if n > 0]
list_2 = [random.randint(1,10) for i in range(1, m+1) if m > 0]

list_1 = set(list_1)
list_2 = set(list_2)

c = list_1.intersection(list_2)

print(list_1) 
print(list_2)
print(c)
# вывод по возрастанию