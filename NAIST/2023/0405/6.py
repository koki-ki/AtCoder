r, g, b, n = map(int, input().split())
ans = 0
max_r = n // r
max_g = n // g

for i in range(max_r + 1):
    for j in range(max_g + 1):
        nokori = n - i * r - j * g
        if nokori % b == 0 and nokori >= 0:
            ans += 1

print(ans)