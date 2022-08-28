n, k, q = map(int, input().split())
p = [0] * n
for _ in range(q):
    answer = int(input())
    p[answer - 1] += 1

for i in range(n):
    if p[i] > q - k: print('Yes')
    else: print('No')
