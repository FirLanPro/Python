# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

n = int(input('Введите сколько км в день проезжает машина:'))
m = int(input('Введите расстояние в км :'))

res = (m + n -1) // n
print(res)