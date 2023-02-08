def match_or_not(a, b):
    return a == '?' or b == '?' or a == b
# main
s = list(input())
t = list(input())

pre = [False for _ in range(len(s) + 1)]
suf = [False for _ in range(len(s) + 1)]

pre[0] = True

for i in range(len(t)):
    if not match_or_not(s[i], t[i]):
        break
    pre[i + 1] = True

s.reverse()
t.reverse()

suf[0] = True
for i in range(len(t)):
    if not match_or_not(s[i], t[i]):
        break
    suf[i + 1] = True

for i in range(len(t) + 1):
    if pre[i] and suf[len(t) - i]:
        print('Yes')
    else:
        print('No')