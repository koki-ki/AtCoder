n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = (1 + k) * k // 2
nums = set()

for ai in a:
    if ai not in nums and 1 <= ai <= k:
        nums.add(ai)
        ans -= ai

print(ans)
