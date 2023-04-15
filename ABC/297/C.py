h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))

for i in range(h):
    for j in range(w - 1):
        if s[i][j] == 'T' and s[i][j + 1] == 'T':
            s[i][j] = 'P'
            s[i][j + 1] = 'C'

for i in range(h):
    ans = ''.join(s[i])
    print(ans)