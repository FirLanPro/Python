# словарь
dictionary = {}
dictionary = {'up': 'ввех', 'left': 'в лево', 'down': 'вниз', 'right': 'в право'}
print(dictionary)
dictionary[895] = 54353 # добавление в словарь
print(dictionary)
# удаление ключа(элемента)
del dictionary['left']
print(dictionary)

# вывод через цикл
for item in dictionary:
    print('{}:{}'.format(item,dictionary[item])) # ключ: значение
    print(item) # вывод ключа

# вывод через цикл
for (k, v) in dictionary.items():
    print(k, v)