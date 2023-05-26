# кортежи. неизменяемые элементы. индексируемые. элементы не уникальные. (). tuple()

t = () # класс кортеж
print(type(t))

t = (1) # класс int
print(type(t))

t = (1,3,4,) # класс кортеж
print(type(t))

# список поменять на кортеж
v = [1,2,3,4,4]
print(v)
print(type(v))
v = tuple(v)
print(v)
print(type(v))
