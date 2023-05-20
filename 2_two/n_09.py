# дробное в целочисленное

n = 5.89
print (n)
print(type(n)) # float

n1 = int (n) # остаётся часть дробного до точки. целая часть. не округление дроби
print(n1)
print(type(n1)) # int

n2 = str(n1) # создание строки
print(n2 + '48sss') # + либо число, либо текст. или число с текстом
print(type(n2)) # str

# class bool
# n = bool(n)
# print(n)
# print(type(n))
