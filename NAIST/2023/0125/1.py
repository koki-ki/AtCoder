n, x = map(int, input().split())
m = []
for i in range(n):
    mi = int(input())
    x -= mi
    m.append(mi)
m.sort()
ans = n
ans += x // m[0]
print(ans)
