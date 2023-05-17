def check(a):
    length = len(a)
    for i in range(length - 1):
        if abs(a[i] - a[i + 1]) != 1:
            return i
    return -1

n = int(input())
a = list(map(int, input().split()))

while check(a) != -1:
    i = check(a)
    if a[i] < a[i + 1]:
        a = a[:i + 1] + list(range(a[i] + 1, a[i + 1])) + a[i + 1:]
    else:
        a = a[:i + 1] + list(range(a[i] - 1, a[i + 1], -1)) + a[i + 1:]

print(*a)
