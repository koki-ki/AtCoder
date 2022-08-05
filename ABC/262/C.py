n = int(input())
INF = 10 ** 9
a = [0]
a_ = list(map(int, input().split()))
a.extend(a_)
mat = [[0] * (n + 1) for _ in range(n + 1)]
ans = 0
naname = 0
kumi = 0

for i in range(1, n + 1):
    if i == a[i]:
        naname += 1

    elif a[i] ==  a[a[i]]:
        kumi += 1

if naname != 0:
    ans += naname * (naname - 1) // 2

ans += kumi

print(ans)
