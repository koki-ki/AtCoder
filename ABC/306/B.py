a = list(map(int, input().split()))
ans = 0

for i, ai in enumerate(a):
    ans += ai * 2 ** i

print(ans)