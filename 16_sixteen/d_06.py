# набор чисел разделённых через пробел, превратить в лист чисел
# select можно заменить на map

list_1 = '15 156 96 3 5 8 52 5'
print(list_1)

# list_1 = list_1.split()
# print(list_1)

list_1 = list(map(int, list_1.split()))
print(list_1)

