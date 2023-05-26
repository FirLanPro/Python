# операции со множествами
a = {1,2,3,4,5,6}
b = {1,2,3,4,8,9}
c = a.copy() # скопировать в с значения а
u = a.union(b) # объединение a и b, уникальные значения для вывода
i = a.intersection(b) # пересечение a и b. пересекающиеся значения
dl = a.difference(b) # разность a-b.
dr = b.difference(a) # b-a
q = a.union(b).difference(a.intersection(b))