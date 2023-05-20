# работает при соблюдении регистра при вводе
username = input('Веедите имя: ')
if username == 'Маша':
    print('Hello, Masha')
elif username == 'Марина':
    print('Marina, hello!')
elif username == 'Ильнар':
    print('ILNAR, HELLO')
else:
    print('Hi, ' , username)