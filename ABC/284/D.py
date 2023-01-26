from math import sqrt
t = int(input())
INF = 9 * 10 ** 18
anses = []
for _ in range(t):
    n = int(input())
    for x in range(2, INF):
        if n % x:
            continue
        n //= x
        if n % x == 0:
            anses.append([x, n // x])
            break
        p = int(sqrt(n))
        anses.append([p, x])
        break

for ans in anses:
    print(*ans)
