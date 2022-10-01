import math
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += 1
    print(i, math.sqrt(i), math.sqrt(i) % 1)
    if math.sqrt(i) % 1 == 0 and i != 1:
        ans += 2

print(ans)