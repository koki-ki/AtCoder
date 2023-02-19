n, k = map(int, input().split())
h = list(map(int, input().split()))
c = [10 ** 9 for _ in range(n)]
c[0] = 0

for i in range(1, n):
    for j in range(i - 1, i - k - 1, -1):
        if j < 0:
            break
        else:
            c[i] = min(c[i], c[j] + abs(h[i] - h[j]))
print(c[-1])