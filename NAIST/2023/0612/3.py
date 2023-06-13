h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

rows_count = [c[i].count('#') for i in range(h)]
columns_count = [sum([1 for j in range(h) if c[j][i] == '#']) for i in range(w)]

ans = 0

num_black = sum(rows_count)

for i in range(2 ** h):
    for j in range(2 ** w):
        tmp = num_black
        checked_rows = set()
        checked_columns = set()
        for l in range(h):
            tmp -= rows_count[i>>l&1]
            if i>>l&1:
                checked_rows.add(l)
        for l in range(w):
            tmp -= columns_count[i>>l&1]
            if i>>l&1:
                checked_columns.add(l)
        for l in checked_rows:
            for m in checked_columns:
                tmp += c[l][m] == '#'


        if tmp == k:
            ans += 1

print(ans)