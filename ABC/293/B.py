n = int(input())
a = [0] + list(map(int, input().split()))
called = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if not called[i]:
        called[a[i]] = True
not_called = []
num = 0
for i in range(1, n + 1):
    if not called[i]:
        not_called.append(i)
        num += 1
print(num)
print(*not_called)