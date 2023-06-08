a = [1,2,3,4,2,1,5,3,2,1,5,3,2,5,5,5]

for i in range(len(a)):
    if a[i] == max(a):
        a[i] = min(a)
print(a)