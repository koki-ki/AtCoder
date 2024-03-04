n = int(input())
x = [0] + list(map(int, input().split()))
x.sort()
ans = 0
for i in range(n + 1, 4 * n + 1):
    ans += x[i]

ans /= 3 * n
print(ans)
