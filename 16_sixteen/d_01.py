def f(x):
    return x*x
a = f     # переименовали f
print(a(5)) # вывод переимнованой; a хранит ссылку на f
print(f(5)) # вывод функции f
print(type(f)) # вывод названия класса; определить класс f