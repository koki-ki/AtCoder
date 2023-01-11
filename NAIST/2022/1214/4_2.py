a, k = map(int, input().split())
NICHO = 2 * (10 ** 12)

n = 0
if k == 0:
    n = NICHO - a
    print(n)
    exit()

while a < NICHO:
    a += 1 + k * a
    n += 1

print(n)