# рекурсия

# возведение числа в степень. a и b целые неотрицательные числа
def Degree(a, b):
    if b > 0:
        return a * Degree(a, b-1)
    else:
        return 1

# сумма чисел. 
def Sum(a, b):
    if b == 0:
        return a
    return Sum(a+1, b-1)