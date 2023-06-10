# В списке хранятся числа.
# Нужно выбрать только чётные числа
# и составить список пар (число, квадрат числа)
# 1 2 3 5 8 15 23 38
# [(2,4),(8,64),(38,1444)]

# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in list_1:
#     if i % 2 == 0:
#         res.append((i,i**2))
# print(res)

def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]

list_2 = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, list_2)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
