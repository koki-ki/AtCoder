n, a, b = map(int, input().split())
s = input()
ans = 5000 * 10 ** 9

for i in range(n):
    cand = a * i
    for j in range(len(s) // 2 + 1):
        if s[(i + j) % len(s)] != s[(-len(s) + i)]:
            cand += b

    ans = min(ans, cand)

print(ans)
