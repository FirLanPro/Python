# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

a = int(input('Сколько учеников в 1 классе: '))
b = int(input('Сколько учеников в 2 классе: '))
c = int(input('Сколько учеников в 3 классе: '))

n = 2

res = (a+1)//n + (b+1)//n + (c+1)//n
print(res)