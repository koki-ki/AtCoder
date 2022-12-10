from collections import defaultdict
n, k, d = map(int, input().split())
a = list(map(int, input().split()))

surpluses = defaultdict(list)
for ai in a:
    surpluses[ai % d].append(ai)


