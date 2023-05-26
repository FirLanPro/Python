# генератор списка
#  создать список,
#  состоящий из четных чисел 
# в диапозоне от 1 до 100

# 1 способ
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)

# 2 сплсоб
list_1 = [i for i in range(1, 101)]
print(list_1)

# вывод чётных чисел
list_1 = [i for i in range(1, 101) if i % 2 == 0]
print(list_1)

# пары чисел
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(list_1)

# умнож, деление, +, -.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)