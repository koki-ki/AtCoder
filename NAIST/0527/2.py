from re import A


a, b = map(int, input().split())
all = 1
ans = 0
while all < b:
    all += -1 + a
    ans += 1

print(ans)
