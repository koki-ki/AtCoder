from collections import defaultdict

nums = list(map(int, list(input())))
mods = defaultdict(int)
for num in nums:
    mods[num % 3] += 1

ans = 20
for i in range(mods[1] + 1):
    for j in range(mods[2] + 1):
        if (mods[1] + mods[2] * 2 - i - 2 * j) % 3 == 0:
            ans = min(ans, i + j)
if ans == len(nums):
    ans = -1
print(ans)
