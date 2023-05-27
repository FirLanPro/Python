# В настольной игре Скрабл (Scrabble) 
# каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
#  B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, 
# которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# ноутбук
#     12

list_1 = input('введите слово только на русском или только на английском: ')
list_2 =list_1.lower()

count = 0

n = len(list_2)
for i in n:
    if 'A' or 'E' or 'I' or 'O' or 'U' or 'L' or 'N'or 'S' or 'T' or 'R' in list_1[i]:
        count += 1
        print(count)
    if 'D' or 'G' in list_1[i]:
        count += 2 
        print(count)
print(count)



