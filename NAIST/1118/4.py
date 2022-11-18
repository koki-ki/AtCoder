n, x, y, z = map(int, input().split())
a = [-1] + list(map(int, input().split()))
b = [-1] + list(map(int, input().split()))
s = [-1] + [a_ + b_ for a_, b_ in zip(a[1:], b[1:])]
scorebook = []
ans = []
for i in range(1, n + 1):
    scorebook.append((i, a[i], b[i], s[i]))

scorebook.sort(key=lambda x: x[0], reverse=True)

scorebook.sort(key=lambda x: x[1])
for i in range(x):
    ans.append(scorebook.pop(-1)[0])

scorebook.sort(key=lambda x: x[0], reverse=True)

scorebook.sort(key=lambda x: x[2])
for i in range(y):
    ans.append(scorebook.pop(-1)[0])

scorebook.sort(key=lambda x: x[0], reverse=True)
scorebook.sort(key=lambda x: x[3])

for i in range(z):
    ans.append(scorebook.pop(-1)[0])

ans.sort()
for i in range(x + y + z):
    print(ans[i])
