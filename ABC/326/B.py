def check(n):
    n_str = str(n)
    a = int(n_str[0])
    b = int(n_str[1])
    c = int(n_str[2])
    return a * b == c


n = int(input())
i = n
while True:
    if check(i):
        print(i)
        exit()
    i += 1
