n = int(input())
a = list(map(int, input().split()))
two = [0] * n
three = [0] * n
ans = 0

for i in range(n):
    while (a[i] % 2 == 0):
        two[i] += 1
        a[i] //= 2

    while (a[i] % 3 == 0):
        three[i] += 1
        a[i] //= 3


a = list(set(a))
if len(a) > 1:
    print(-1)
    exit()
m2 = min(two)
m3 = min(three)
for i in range(n):
    ans += two[i] - m2
    ans += three[i] - m3
print(ans)

