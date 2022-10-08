n = int(input())
a = [False] * (n + 2)
for i in map(int, input().split()):
    a[min(n + 1, i)] = True

read = 0
while n >= 0:
    read += 1
    n -= 1 if a[read] else 2

print(read - 1)
