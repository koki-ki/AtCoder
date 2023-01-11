n, m = map(int, input().split())
ans = 0
if 2 * n > m:
    ans = m // 2
elif 2 * n == m:
    ans = n
else:
    ans += n
    m -= 2 * n
    ans += m // 4
print(ans)
