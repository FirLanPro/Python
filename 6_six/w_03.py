# дано n(список из целых чисел) и k(положительное число), 
# сдвинуть всю последовательность на k элементов вправо. сдвиг циклический.
## переместить k элементов с конца в начало.

myList = [1, 2, 3, 6, 7,-9, 0]
n = int(input('введите сдвиг: ')) % len(myList)
for i in range(n):
    myList.insert(0, myList.pop())
print(myList)