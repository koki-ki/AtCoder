n = int(input())
a = [0] + list(map(int, input().split()))

num_of_same = 0
for i in range(1, n + 1):
    if a[i] == i:
        num_of_same += 1
ans = num_of_same * (num_of_same - 1) // 2

for i in range(1, n + 1):
    if a[i] > i and a[a[i]] == i:
        ans += 1

print(ans)
