from collections import deque

q = int(input())
cylinder = deque()

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x, c = query
        last = cylinder.pop()


    else:
        _, c = query