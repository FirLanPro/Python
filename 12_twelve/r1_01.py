def LastFibo(n):
    if n in [0, 1]:
        return n
    return LastFibo(n-1) + LastFibo(n-2)

def revense_range(num):
    print(num, end = " ")
    if num > 0:
        revense_range(num -1)
    