from collections import defaultdict

n = int(input())
d = defaultdict(str)
start = set()
for i in range(n):
    s, t = input().split()
    d[s] = t
    start.add(s)

visited = set()
for start_step in start:
    next_step = d[start_step]
    while next_step not in visited:
        visited.add(next_step)
        if next_step == '':
            break
        next_step = d[next_step]
        if next_step == start_step:
            print('No')
            exit()
print('Yes')