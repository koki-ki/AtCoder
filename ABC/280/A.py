h, w = map(int, input().split())
ans = 0
for _ in range(h):
    s = list(input())
    ans += s.count('#')
print(ans)
