from itertools import combinations
n, m = map(int, input().split())
nums = [i for i in range(1, m + 1)]
tanchouzouka = list(combinations(nums, n))
for t in tanchouzouka:
    print(*t)
