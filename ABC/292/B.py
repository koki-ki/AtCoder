n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]
cards = [0 for _ in range(n + 1)]
for query in queries:
    c, x = query
    if c == 1:
        cards[x] += 1
    elif c == 2:
        cards[x] += 2
    else:
        if cards[x] >= 2:
            print('Yes')
        else:
            print('No')


