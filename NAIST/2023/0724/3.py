import heapq

n = int(input())
a = list(map(int, input().split()))
ans = 0

nums = set(list(range(1, 10001)))
for ai in a:
    if ai in nums:
        nums.remove(ai)

nums = list(nums)
heapq.heapify(nums)

for i in range(n - 1):
    if a[i] == a[i + 1]:
        ans += 1
        a[i + 1] = heapq.heappop(nums)

print(ans)
