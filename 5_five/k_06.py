# распаковка кортежа
v = (1,2,3,)
a,b,c = v
print(a,b,c)

#
print(v[1]) # вывод элемента с индексом 1

#вывод элементов не след строке
for i in v:
    print(i)

# 2 способ. вывод элементов не след строке
for i in range(len(v)):
    print(v[i])