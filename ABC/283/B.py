n = int(input())
a = list(map(int, input().split()))
q = int(input())
ans = []
for _ in range(q):
    query = list(input().split())
    if query[0] == '1':
        k = int(query[1])
        k -= 1
        x = int(query[2])
        a[k] = x
        pass
    else:
        k = int(query[1])
        k -= 1
        ans.append(a[k])

for a in ans:
    print(a)
