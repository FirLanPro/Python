# Требуется вычислить, 
# сколько раз встречается некоторое число X ??
# в массиве A[1..N].
# Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# 5
#     1 2 3 4 5
#     3
#     -> 1

# рандомный массив от 1 по 10

import random

n = int(input('количество элементов в массиве, (натуральное число): '))
list_1 = [random.randint(1,10) for i in range(1, n+1) if n > 0]
print(*list_1)
if n <= 0:
    print('натуральное число от 1 и выше')
else:
    x = int(input('некоторое число X: '))
    count = 0
    for i in range(n):
        if list_1[i] == x:
            count +=1

    print('встречается', count, 'раз(а)')


