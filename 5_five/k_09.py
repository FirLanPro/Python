# множества. неизменяемые. не индексируемые. уникальные. {}. set()

colors = {'red', 'green', 'blue'}
print(colors)
colors.add('gray') # добавление
print(colors)

colors.remove('red')
print(colors) # удаление 

colors.discard('red') # поверка и удаление. элемента нет - пропускает
print(colors)

colors.clear() # удаление всех элементов 
print(colors) # и вывод set() - пустое множество

q = set()

