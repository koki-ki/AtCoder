from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = deque()

for i in range(n):
    if i % 2 == 0:
        b.appendleft(a[i])
    else:
        b.append(a[i])
b = list(b)
if n % 2 == 0:
    print(*b[::-1])
else:
    print(*b)