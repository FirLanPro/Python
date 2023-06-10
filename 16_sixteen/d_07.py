# вывод элементов оканчивающихся на 5, из списка
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]

res = list(filter(lambda x: x % 10 == 5, list_1))
print(res)