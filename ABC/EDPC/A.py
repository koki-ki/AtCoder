n = int(input())
h = list(map(int, input().split()))
c = [10 ** 9 for _ in range(n)]
c[0] = 0
c[1] = abs(h[1] - h[0])
for i in range(n - 2):
    c[i + 2] = min(c[i] + abs(h[i + 2] - h[i]), c[i + 1] + abs(h[i + 2] - h[i + 1]))
print(c[n - 1])