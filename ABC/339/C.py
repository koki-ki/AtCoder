n = int(input())
a = list(map(int, input().split()))

m = 0
sum_up = 0

for i in range(n):
    sum_up += a[i]
    m = min(m, sum_up)

print(sum_up - m)
