# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

myList = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(myList)):
    if myList[i] > myList[i - 1]:
        count += 1
print(count)

# result = [myList[i] for i in range(1, len(myList)) if myList[i] > myList[i - 1]]
# print(result) # индексы