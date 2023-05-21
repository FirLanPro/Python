# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# петя = серёжа = p
# петя + серёжа = 2p
# катя = 2p * 2 = 4P = k
# s - общее количество целых журавликов
# s = 2p +(4p) = 6p
# s / 6 = p

# общее количество целых журавликов кратно 6
# т.к. подсчёт был уже сделанного,
# у пети и серёжи равное количество целых поделок.

s = int(input('введите общее число журавликов: '))
if s % 6 == 0:
    p = s // 6
    k = 4 * p
    print("петя сделал: ", p ,"журавликов")
    print("серёжа сделал: ", p, "журавликов")
    print("Катя сделала: ", k, "журавликов")
else: 
    print("такое количество журавликов они сделать не могли")
