# последовательный вывод чисел. число на следующей строке.

# через цикл for
for i in 1, 2, 3, 4:
    print(i)

# через range

r = range(5) # вывод от 0 до 4, шаг 1 
r = range(2, 5) # вывод от 2 до 4, шаг 1
r = range(0, -5) # ---- шаг невозможен в сторону увеличения отрицательного
r = range(1, 10, 2) # вывод от 1 до 9, шаг 2 
r = range(100, 0, -20) # вывод от 100 до 1, шаг -20
for i in r:
    print(i)
