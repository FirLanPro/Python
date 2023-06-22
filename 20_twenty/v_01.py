# телефонный справочник
# c возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал
# для изменения и удаления данных

# при условии, что все контакты уникальны.

import os


def show_contacts(file_name):
    os.system("clear")
    with open(file_name, 'r') as file:
        data = file.readlines()
        for contact in data:
            print(contact, end='')
    input('\nнажмите Enter')


def add_contact(file_name):
    os.system("clear")
    with open(file_name, 'a') as file:
        res = ''
        res += input('фамилия  ') + ' '
        res += input('имя  ') + ' '
        res += input('№ телефона  ')

        file.writelines("\n")
        file.writelines(res)

    input('нажмите Enter')

def replace_contact(file_name):
    os.system("clear")
    data = input("введите изменяемые данные :")
    zamen = input(" изменить на : ")
    file_1 = open(file_name).readlines()
    for item in file_1:
        if data in item:
            data_1 = item.replace(data, zamen)
            file_1.remove(item)

    with open(file_name, 'w') as file:
        file.writelines(file_1)
        file.writelines(data_1)

    input('нажмите Enter')


def del_data(file_name):
    os.system("clear")
    target = input(' введите данные для удаления: ')
    file_1 = open(file_name).readlines()
    for item in file_1:
        if target in item:
            list_1 = item.split()
            file_1.remove(item)
        
    with open(file_name, 'w') as file:
        for i in list_1:
            if target == i:
                list_1.remove(i)
        file.writelines(file_1)
        file.writelines('\n')
        file.writelines(" ".join(list_1))


def del_strok_data(file_name):
    os.system("clear")
    target = input(' введите данные строки, для удаления контакта: ')
    file_1 = open(file_name).readlines()
    for item in file_1:
        if target in item:
            file_1.remove(item)
    with open(file_name, 'w') as file:
        file.writelines(file_1)


def drawing():
    print('1-просмотр всех контактов')
    print('2-запись нового контакта')
    print('3-изменение данных контакта, замена')
    print('4-удаление данных из контакта')
    print("5-удаление контакта полностью")
    print('6-выход из программы')


def main(file_name):
    while True:
        os.system("clear")
        drawing()
        user_choice = int(input('введите число от 1 до 6:   '))
        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            replace_contact(file_name)
        elif user_choice == 4:
            del_data(file_name)
        elif user_choice == 5:
            del_strok_data(file_name)
        elif user_choice == 6:
            print('exit')
            return


main('text.txt')
