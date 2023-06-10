
def math_1(op, x, y):
    print(op(x,y))

# сокращение функции def calc_1(a, b): return a + b
calc_2 = lambda a,b: a + b

math_1(calc_2, 5,45)

# ещё короче
math_1(lambda a,b: a + b, 5, 45)