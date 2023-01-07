from collections import deque
a = deque([0])
n = int(input())
s = input()
for i in range(1, n + 1):
    if s[i - 1] == 'L':
        a.insert(a.index(i - 1), i)
    else:
        a.insert(a.index(i - 1) + 1, i)
print(*a)
