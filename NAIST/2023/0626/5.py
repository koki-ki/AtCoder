
n, k = map(int, input().split())
r, s, p = map(int, input().split())
score = {'r': p, 's': r, 'p': s}

t = list(input())
ans = 0

for k_ in range(k):
    for i in range(k_, n, k):
        if i >= k and t[i - k] == t[i] and last:
            last = False
        else:
            ans += score[t[i]]
            last = True

print(ans)