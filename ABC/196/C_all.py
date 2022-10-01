from math import sqrt
n = int(input())
ans = 0
for i in range(1, int(sqrt(n)) + 1):
    num = int(str(i) * 2)
    if num <= n:
        ans += 1
print(ans)