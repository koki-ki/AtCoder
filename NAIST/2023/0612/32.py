from copy import deepcopy

h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

rows_count = [c[i].count('#') for i in range(h)]
columns_count = [sum([1 for j in range(h) if c[j][i] == '#']) for i in range(w)]

ans = 0

num_black = sum(rows_count)

for i in range(2 ** h):
    for j in range(2 ** w):
        tmp_c = deepcopy(c)
        for l in range(h):
            for m in range(w):
                tmp = tmp - rows_count[i>>l&1] - columns_count[j>>m&1] + (1 if c[l][m] == '#' else 0)

        if tmp == k:
            ans += 1

print(ans)