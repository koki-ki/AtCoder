n = int(input())
sum = 0
for _ in range(n):
    a, b = map(int, input().split())
    sum += a * b
sum *= 1.05
sum = int(sum)
print(sum)
