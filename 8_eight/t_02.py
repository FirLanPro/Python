#  Требуется найти в массиве A[1..N] 
#  самый близкий по величине элемент к заданному числу X. 
#  Пользователь в первой строке
#  вводит натуральное число N – количество элементов в массиве. 
#  В последующих  строках записаны N целых чисел Ai. 
#  Последняя строка содержит число X

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input('количество элементов в массиве: '))
list_1 = [random.randint(1,10) for i in range(1, n+1) if n > 0]
print(*list_1)
x = int(input('некоторое число X: '))
count = 0
count_1 = 0
for i in range(n):
   if  count < list_1[i] < x:
        count = list_1[i]
   if count < list_1[i] > x:
        count_1 = list_1[i]

m = (count_1-count) // 2
for i in range(1,m+1):
    if x-i != count:
        print('4444',count)
    if x+i != count_1:
        print('555',count_1)
    if  x+1 == x-1:
        print('666',count_1,count)

print('111',m)
print('2222',count)
print('3333',count_1)

