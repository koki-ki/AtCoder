n, m = map(int, input().split())
a = list(map(int, input().split()))

vote = [0 for _ in range(n + 1)]
ans = 0

for i in range(m):
    vote[a[i]] += 1
    if vote[ans] < vote[a[i]]:
        ans = a[i]
    elif vote[ans] == vote[a[i]] and a[i] < ans:
        ans = a[i]
    print(ans)
