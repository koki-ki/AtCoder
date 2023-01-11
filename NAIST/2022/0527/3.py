n = int(input())
a = list(map(int, input().split()))

manzoku = []
ireru = 1
for i in range(n):
    if ireru == a[i]:
        manzoku.append(ireru)
        ireru += 1

ans = n - len(manzoku)
if ans == n:
    print(-1)
else:
    print(ans)