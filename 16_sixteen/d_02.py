def calc_1(a):
    return a + a
def calc_2(a):
    return a * a

def math(op, x):
    print(op(x))

def calc_3(a, b):
    return a + b
def math_2(op, x, y):
    print(op(x,y))

math(calc_1, 5) # передали функции math, функцию calc_1
math(calc_2, 5) # передали функции math, функцию calc_2
math_2(calc_3, 5, 45) # передали функции math_2, функцию calc_3
