# сумма всех элементов от 1 до n. функция sumNumbers(n).
def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)
sum_numbers(5)

# return
def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sum_numbers(5)
print(a)

# 2 аргумента функции
def sum_numbers(n, y = "Hello"):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sum_numbers(5)
print(a)
#
def sum_numbers(n,y):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sum_numbers(5, "qwerty")
print(a)