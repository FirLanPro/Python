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

# если в слове есть и англ и рус буквы, или другие символы, result возвращает 0.

text = input('введите одно слово только на русском или только на английском: ')
list_1 = text.upper()
list_2 = text.lower()

eng = 'qwertyuiopasdfghjklzxcvbnm'

rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

en_list = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
        4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
 
rus_list= {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 
        4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

length = len(text)
length_text = 0
length_text_2 = 0
result = 0

for i in list_2:
    if i in eng:
        length_text += 1
        if length_text == length:
            print('EN')
            result = sum([key for j in list_1 for key, value in en_list.items() if j in value])
    elif i in rus:
        length_text_2 += 1
        if length_text_2 == length:
            print('rus')
            result = sum([key for j in list_1 for key, value in rus_list.items() if j in value]) 

print(result)
            
 