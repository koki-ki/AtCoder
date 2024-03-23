INF = 10 ** 18

n = int(input())
s = input()
c = list(map(int, input().split()))

cost_01 = [0] * (n + 1)
cost_10 = [0] * (n + 1)

for i in range(n):
    char_01 = "0" if i % 2 == 0 else "1"
    char_02 = "1" if i % 2 == 0 else "0"
    cost_01[i] = c[i] if s[i] != char_01 else 0
    cost_10[i] = c[i] if s[i] != char_02 else 0

ans = INF

cost_01_sum = sum(cost_01)
cost_10_sum = sum(cost_10)

tmp = cost_01_sum

for i in range(n - 1):
    tmp = tmp - cost_01[i] + cost_10[i]
    ans = min(ans, tmp)

tmp = cost_10_sum
for i in range(n - 1):
    tmp = tmp - cost_10[i] + cost_01[i]
    ans = min(ans, tmp)

print(ans)
