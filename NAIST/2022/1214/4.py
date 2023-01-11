def f(n):
    return a * (k + 1) ** n  + n

a, k = map(int, input().split())
n = 0
if k == 0 and a != 0:
    print(2 * 10 ** 12 - a)
    exit()
elif a == 0:
    print(2 * 10 ** 12)
    exit()

while f(n) <= 2 * (10 ** 12):
    n += 1

print(n)
