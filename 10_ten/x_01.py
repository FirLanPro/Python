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

# import random
n = int(input('количество элементов первого множества: '))
m = int(input('количество элементов второго множества: '))

if m > 0 and n > 0:
    list_1 = [input('элемент первого множества: ') for i in range(n)]
    list_2 = [input('элемент второго множества: ') for i in range(m)]

    print(list_1) 
    print(list_2)

    list_3 = set(list_1).intersection(set(list_2))
    print(list_3)

    list_3 = list(list_3)
    length = len(list_3)
    count = length
    storage = 0
    while count > 0:
        for i in range(length-1):
            if list_3[i] > list_3[i+1]:
                storage = list_3[i]
                list_3[i] = list_3[i+1]
                list_3[i+1] = storage
        count -= 1
    print(list_3)
else:
    print("вводите количество элементов значением больше нуля")
