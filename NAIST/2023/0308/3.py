from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
numNums = defaultdict(int)

for a_ in a:
    numNums[a_ - 1] += 1
    numNums[a_] += 1
    numNums[a_ + 1] += 1

print(max(numNums.values()))