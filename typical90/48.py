n, k = map(int, input().split())
scores = []
for i in range(n):
    a, b = map(int, input().split())
    scores.append(b)
    scores.append(a - b)
scores.sort(reverse=True)
ans = sum(scores[:k])
print(ans)
