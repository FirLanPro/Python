# Требуется определить,
# можно ли от шоколадки размером n × m долек 
# отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes 
# 3 2 1 -> no

# общее количество долек: p
# отломить K долек


n = int(input('n:'))
m = int(input('m:'))
k = int(input('k:'))
if n != 0 and m != 0:
    if k % 2 == 0:
        if n == k or m == k:
            print("yes")
        elif n>k or m>k:
            print("no")
        elif k < m * n:
            if k % m ==0 or k % n ==0:
                print("yes")
        else: print("no")
        k = k + 1
    elif n == k or m == k:
        print("yes")
    else: print("no")
else: print("шоколада нет")

