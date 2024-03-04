a, b = map(int, input().split())
while a > 0 or b > 0:
    if a % 10 + b % 10 >= 10:
        print("Hard")
        exit()
    else:
        a //= 10
        b //= 10

print("Easy")