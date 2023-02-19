n = int(input())
a = list(map(int, input().split()))
c = [10 ** 9 for _ in range(n)]
c[0] = 0
c[1] = abs(a[1] - a[0])
for i in range(n - 2):
    c[i + 2] = min(c[i] + abs(a[i + 2] - a[i]), c[i + 1] + abs(a[i + 2] - a[i + 1]))
print(c[-1])