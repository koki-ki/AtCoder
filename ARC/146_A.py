from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
a.sort()
num = 0
for v in permutations(a[-3:], 3):
    nnum = int(str(v[0]) + str(v[1]) + str(v[2]))
    num = max(num, nnum)
print(num)
