n, m, x, t, d = map(int, input().split())
ans = t if m >= x else t - d * (x - m)
print(ans)
