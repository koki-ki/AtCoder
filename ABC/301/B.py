def check(a):
    n = len(a)
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) != 1:
            return i
    return -1

n = int(input())
a = list(map(int, input().split()))

while check(a) != -1:
    i = check(a)

    if a[i] < a[i + 1]:
        tbi = list(range(a[i] + 1, a[i + 1]))
    else:
        tbi = list(range(a[i] - 1, a[i + 1], -1))
    a = a[:i + 1] + tbi + a[i + 1:]

print(*a)
