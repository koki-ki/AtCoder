n, q = map(int, input().split())
queries = list(list(map(int, input().split())) for _ in range(q))

front = [-1 for _ in range(n + 1)]
back = [-1 for _ in range(n + 1)]

for i in range(q):
    if queries[i][0] == 1:
        x, y = queries[i][1:]
        front[y] = x
        back[x] = y
    elif queries[i][0] == 2:
        x, y = queries[i][1:]
        front[y] = -1
        back[x] = -1
    else:
        x = queries[i][1]
        # 前に行く
        while front[x] != -1:
            x = front[x]
        # 後ろに行きながら答えを追加していく
        ans = []
        while x != -1:
            ans.append(x)
            x = back[x]
        print(len(ans), end=' ')
        for a in ans:
            print(a, end=' ')
        print()
