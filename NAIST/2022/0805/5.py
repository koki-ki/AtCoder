N = int(input())

data = [0] * (N + 1)
ruiseki = [0] * (N + 1)
last_day = 0
for _ in range(N):
    a, b = map(int, input().split())
    data[a] += 1
    data[a + b] -= 1
    last_day = max(last_day, a + b)

for i in range(1, last_day):
    ruiseki[i] = ruiseki[i - 1] + data[i]

print(ruiseki)

