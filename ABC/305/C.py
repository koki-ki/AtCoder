h, w = map(int, input().split())
s = ['.' * (w + 2)]
for _ in range(h):
    s.append('.' + input() + '.')
s.append('.' * (w + 2))

for i in range(1, h + 1):
    for j in range(1, w + 1):
        # 中
        if s[i][j - 1] == '#' and s[i][j] == '.' and s[i][j + 1] == '#':
            ans_i = i
            ans_j = j
            break
        if s[i - 1][j] == '#' and s[i][j] == '.' and s[i + 1][j] == '#':
            ans_i = i
            ans_j = j
            break
        if (s[i][j] == '.' and s[i][j + 1] == '#' and s[i + 1][j] == '#') or \
        (s[i][j] == '.' and s[i][j - 1] == '#' and s[i + 1][j] == '#') or \
        (s[i][j] == '.' and s[i - 1][j] == '#' and s[i][j + 1] == '#') or \
        (s[i][j] == '.' and s[i][j - 1] == '#' and s[i-1][j] == '#'):
            ans_i = i
            ans_j = j
            break


print(ans_i, ans_j)