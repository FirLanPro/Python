# Создать телефонный справочник 
# с возможностью импорта и экспорта данных в
# формате .txt.
# Фамилия, имя, отчество, номер телефона 
# - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')

    input('\n!!!!!!!!!!')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('фамилия  ') + ' '
        res += input('имя  ') + ' '
        res += input('№ телефона  ')

        file.write('\n'+ res )

    input('!!!!!!!!!!')

def search_contact(file_name):
    os.system('CLS')
    target = input(' имя ')

    with open(file_name, 'r' ) as file:
        contacts = file.readlines()
        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print('контакта с таким именем нет')

    input('!!!!!!!!!!')

def drawing():
    print('1-show contacts')
    print('2-add contacts')
    print('3-search contacts')
    print('4-exit contacts')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('введите число от 1 до 4   '))
        
        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            print('exit')
            return

main('text.txt')

#show_contacts("text.txt")

