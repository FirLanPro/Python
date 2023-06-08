# напишите функцию, которая принимает число 
# и проверяет является оно простие или нет.

number = int(input("введите число: "))
def is_simple(number):
    if number > 2 and number % 2 != 0: # от тройки и более
        for i in range(3, number // 2):
            if number % i == 0:
                return False
        return True
    return False
print(is_simple(number))
