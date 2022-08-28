n = int(input())
a = list(map(int, input().split()))
p = 0

masu = [0] * n

for i in range(n):
    for j in range(0, i + 1):
        masu[j] += a[i]

ans = sum([1 for x in masu if x > 3])
print(ans)

