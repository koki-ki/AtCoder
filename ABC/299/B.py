n, t = map(int, input().split())
c = [0] + list(map(int, input().split()))
r = [0] + list(map(int, input().split()))

cands1 = []
cands2 = []

for i in range(1, n + 1):
    if c[i] == t:
        cands1.append([i, r[i]])
    if c[i] == c[1]:
        cands2.append([i, r[i]])

if cands1 != []:
    ans = 0
    maxv = 0
    for i, r in cands1:
        if maxv < r:
            ans = i
            maxv = r

else:
    ans = 0
    maxv = 0
    for i, r in cands2:
        if maxv < r:
            ans = i
            maxv = r

print(ans)