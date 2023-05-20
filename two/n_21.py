# срезы
text = 'AbcdeiFghijkLmnopqrsTuvwxyz'
print(text[0]) # первый символ
print(text[1]) # второй символ
print(text[len(text)-1]) # последний символ
print(text[-1]) # последний символ
print(text[-5]) # 5 символ с конца
print(text[:]) # вывод всех символов
print(text[:2]) # вывод с 0 до 2 элемента(0, 1)
print(text[len(text)-2:]) # вывод от 3 с конца и до конца
print(text[20:]) # с 20 элемента и до конца
print(text[2:9])# с 2 до 9 элемента
print(text[6:-18])# с 6 и по -18 элемент с конца
print(text[0:len(text):6])# от 0 до конца с шагом 6
print(text[::6])# от 0 до конца с шагом 6

text = text[2:9] + text[-5] + text [:2] # сложение интервалов текста
print(text)