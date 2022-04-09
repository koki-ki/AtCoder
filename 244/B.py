import numpy as np
n = int(input())
t = input()
xy = np.array([0, 0])
muki = np.array([[1, 0], [0, -1], [-1, 0], [0, 1]])
j = 0
for i in range(n):
    if t[i] == 'S':
        xy += muki[j % 4]
    else:
        j += 1

print(xy[0], xy[1])