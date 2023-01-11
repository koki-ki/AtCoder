def marubatu(s, t):
    can_solve = ''
    for i in range(len(s)):
        if s[i] == 'o' or t[i] == 'o':
            can_solve += 'o'
        else:
            can_solve += 'x'
    return can_solve


# main #
n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
ans = 0


for x in range(n):
    for y in range(n):
        if x == y:
            continue

        can_solve = marubatu(s[x], s[y])
        if can_solve == 'o' * m:
            ans += 1
ans //= 2
print(ans)
