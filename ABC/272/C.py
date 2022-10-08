N = int(input())
A = list(map(int, input().split()))

odds = []
evens = []
A.sort()

for a in A:
    if a % 2 == 0:
        evens.append(a)
    else:
        odds.append(a)

candidates = []

try:
    candidates.append(odds[-1] + odds[-2])
except:
    pass
try:
    candidates.append(evens[-1] + evens[-2])
except:
    pass

if len(candidates) == 0:
    print(-1)
else:
    print(max(candidates))