q = int(input())
a = []
for _ in range(q):
    query = list(map(int, input().split()))
    _, x = query
    if query[0] == 1:
        a.append(x)
    else:
        _, k = query
        print(a[-k])
