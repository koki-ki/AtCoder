n = int(input())
a = [0] + list(map(int, input().split()))
s = [None for _ in range(n)]
t = [None for _ in range(n)]

for i in range(1, n):
    s[i], t[i] = map(int, input().split())

for i in range(1, n):
    a[i + 1] += a[i] // s[i] * t[i]

print(a[n])
