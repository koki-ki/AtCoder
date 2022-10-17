n = int(input())
a = list(map(int, input().split()))

cnts = {}

for i in range(n):
    if a[i] not in cnts.keys():
        cnts[a[i]] = 1
    else:
        cnts[a[i]] += 1

cnts = sorted(cnts.items(), reverse=True)


ans = []
for i in range(len(cnts)):
    ans.append(cnts[i][1])
nokori = n - len(ans)
for i in range(len(ans)):
    print(ans[i])
for i in range(nokori):
    print(0)
