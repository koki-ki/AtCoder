n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

connected_nodes = [set() for _ in range(n + 1)]
zero_nodes = set([i for i in range(1, n + 1)])

for query in queries:
    if query[0] == 1:
        u, v = query[1:]
        connected_nodes[u].add(v)
        connected_nodes[v].add(u)
        if u in zero_nodes:
            zero_nodes.remove(u)
        if v in zero_nodes:
            zero_nodes.remove(v)
    else:
        v = query[1]
        for u in connected_nodes[v]:
            connected_nodes[u].remove(v)
            if len(connected_nodes[u]) == 0:
                zero_nodes.add(u)
        connected_nodes[v] = set()
        zero_nodes.add(v)

    ans = len(zero_nodes)
    print(ans)