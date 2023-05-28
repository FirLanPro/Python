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

number = 10
n = int(input('количество элементов в массиве: '))
list_1 = [random.randint(1,number) for i in range(1, n+1) if n > 0]
print(*list_1)
x = int(input('некоторое число X: '))

count = 1
count_1 = 0


for j in range(count+1):
    for i in range(n-1):
        if x - count == list_1[i]:
            count_1 = list_1[i]
        if x + count == list_1[i]:
            count_1 = list_1[i]
    if count_1 == 0:
        count += 1      
print(count_1)
      

# if count_1 != 0 and count_2 != 0:
#     print("2 ближайших по величине элемента")       







