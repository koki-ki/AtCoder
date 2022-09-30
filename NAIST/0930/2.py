from itertools import permutations
a = list(map(int, input().split()))
L = list(permutations(a))
ans = 1000
for l in L:
    cost = abs(l[1] - l[0]) + abs(l[2] - l[1])
    ans = min(ans, cost)
print(ans)
