n = int(input())
a = [0] + list(map(int, input().split())) + [0]

cost = [abs(a[i + 1] - a[i]) for i in range(n + 1)]
print(cost)
