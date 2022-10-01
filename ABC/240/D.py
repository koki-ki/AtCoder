n = int(input())
a = list(map(int, input().split()))
tube = []
ans = 0

for i in range(n):
    tube.append([a[i], 1])
    ans += 1

    if len(tube) >= 2 and tube[-2][0] == tube[-1][0]:
        tube[-2][1] += tube[-1][1]
        tube.pop()

    if tube[-1][1] >= tube[-1][0]:
        ans -= tube[-1][0]
        tube[-1][1] -= tube[-1][0]

    if tube[-1][1] == 0:
        tube.pop()
    print(ans)

