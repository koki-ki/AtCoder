def popcount(x):
    num_one = 0
    while x:
        if x % 2 == 1:
            num_one += 1
        x //= 2
    return num_one

a, b, C = map(int, input().split())

