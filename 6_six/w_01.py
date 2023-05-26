# ввод числа N - общее количество
# рассматриваемых дней (1 <= N <= 100), целые числа
# каждое число - среднесуточная температура в день
# температура в диапозоне от -50 до 50

count = 0
max = 0

n = int(input('введите количество дней: '))
for dayCount in range(n):
    day = int(input('Введите темперетуру: '))
    if day > 0:
        count += 1
    elif count >= max:
        max = count
        count = 0
if count > max:
    max = count

print('max количество дней: ', max) 