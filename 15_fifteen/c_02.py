# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


# приграмма не будет работать, если min or max значения не заданы

list_1 = list(map(int, input("Введите массив, каждое число через пробел: ").split()))

min = int(input("min: "))
max = int(input("max: "))
length = len(list_1)
list_2 = []
if min < max and length > 0 and min != "":
    for i in range(length):
        if min <= list_1[i] <= max:
            list_2.append(i)
    print(*list_2)
else:
    print("в массиве должен быть хотябы один элемент; min и max задают диапозон. не равны друг другу и min < max")
