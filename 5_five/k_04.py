# вывод элементов по индексу. интервалами.
list_1 = [2,3,4,5,6,7,8,9,0,74,57,58,43,37]
print(list_1[0]) # вывод первого элемента
print(list_1[1]) # вывод второго элемента
print(list_1[len(list_1)-1]) # вывод последнего
print(list_1[-1]) # вывод последнего
print(list_1[-5]) # вывод пятого с конца
print(list_1[:]) # вывод списка полностью
print(list_1[:2]) # вывод с начала и до второго индекса
print(list_1[len(list_1)-2:]) # вывод от второго с коца и до конца
print(list_1[2:9]) # вывод от 2 до 9 элемента
print(list_1[0:len(list_1):6]) # вывод с начала и до конца с шагом 6
print(list_1[::6]) # вывод с начала и до конца с шагом 6
