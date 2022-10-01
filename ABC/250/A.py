h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0
if r >= 2:
    ans += 1
if r <= h - 1:
    ans += 1
if c  >= 2:
    ans += 1
if c  <= w - 1:
    ans += 1
print(ans)