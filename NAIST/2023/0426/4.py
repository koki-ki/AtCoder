from itertools import permutations
from math import factorial

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))


p_cands = list(permutations(sorted(p)))
q_cands = list(permutations(sorted(q)))


for i in range(factorial(n)):
    if p_cands[i] == p:
        a = i + 1
    if q_cands[i] == q:
        b = i + 1

print(abs(a - b))