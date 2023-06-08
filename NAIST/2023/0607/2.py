n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0

for i, xi in enumerate(x, 1):
    ans += min(xi * 2, abs(k - xi) * 2)

print(ans)
