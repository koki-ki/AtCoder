S = list(input())
C = list('CODEFESTIVAL2016')
ans = 0
for s, c in zip(S, C):
    if s != c:
        ans += 1
print(ans)
