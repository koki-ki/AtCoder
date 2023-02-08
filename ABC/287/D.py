# main
s = input()
t = input()
lent = len(t)

top = [False for _ in range(lent)]
bottom = [False for _ in range(lent)]

for x in range(lent):
    if s[x] == t[x] or s[x] == '?' or t[x] == '?':
        top[x] = True
    if s[-lent + x] == t[x] or s[-lent + x] == '?' or t[x] == '?':
        bottom[x] = True

top_ok = 0
bottom_ok = 0

for x in range(lent):
    if top[x]:
        top_ok += 1
    else:
        break

for x in range(lent):
    if bottom[x]:
        bottom_ok += 1
    else:
        break

for x in range(lent + 1):
    if 0 <= x <= top_ok and 0 <= lent - x <= bottom_ok:
        print('Yes')
    else:
        print('No')