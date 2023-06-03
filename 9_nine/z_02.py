# Напишите программу, 
# которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам 
# с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

text = input()
my_List = text.split()
list_1 = {}
count = str()
for i in my_List:
    if i in list_1.keys():
        list_1[i] += 1
        count += f'{i}_{list_1[i]} '
    else:
        list_1[i] = 0
        count += f'{i} '
print(text)
print(count)

