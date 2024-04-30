a = list(map(int, input().split()))
b = list(map(int, input().split()))

taka = sum(a)
aoki = sum(b)

if aoki > taka:
    print(0)
else:
    ans = taka - aoki + 1
    print(ans)
