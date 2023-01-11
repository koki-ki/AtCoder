from itertools import permutations
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
nums = list(range(1, n + 1))
Per = list(permutations(nums))

for i, per in enumerate(Per):
    if per == p:
        a = i
    if per == q:
        b = i

print(abs(a - b))
