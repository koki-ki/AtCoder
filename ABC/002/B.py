w = list(input())
ans = ''
for w_ in w:
    if w_ not in list('aiueo'):
        ans += w_
print(ans)
