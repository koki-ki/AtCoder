n = int(input())
honests = []
liars = []
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        if y == 1:
            honests.append(x - 1)
        else:
            liars.append(x - 1)
ans = 0
for msk in range(1 << n):
    ok = True
    tot = 0
    for i in range(n):
        if msk & (1 << i):
            tot += 1
        for honest in honests:
            if (not(msk & (1 << honest))):
                ok = False
        for liar in liars:
            if(msk & (1 << liar)):
                ok = False
    if ok:
        ans = max(ans, tot)
print(ans)
