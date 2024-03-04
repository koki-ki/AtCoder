from collections import deque

n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

queue = deque(a)
print(queue)