# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = input('введите число: ')
length= len(number)
summa = 0
k = range(length)
if length == 3:
    for i in k:
        s = int(number[i])
        summa += s
    print(summa) 
else: print('не трёхзначное число')

