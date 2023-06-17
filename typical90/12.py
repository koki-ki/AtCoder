class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    def same(self, u, v):
        return self.root(u) == self.root(v)


def query1(px, py):
    px, py = px - 1, py - 1
    hash1 = px * w + py
    painted[hash1] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for ddx, ddy in zip(dx, dy):
        qx = px + ddx
        qy = py + ddy
        hash2 = qx * w + qy
        if 0 <= hash2 < h * w:
            if painted[hash2]:
                uf.unite(hash1, hash2)


def query2(px, py, qx, qy):
    px, py, qx, qy = px - 1, py - 1, qx - 1, qy - 1
    hash1 = px * w + py
    hash2 = qx * w + qy
    if painted[hash1] and painted[hash2] and uf.same(hash1, hash2):
        return True
    else:
        return False


h, w = map(int, input().split())
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
uf = UnionFind(h * w)
painted = [False for _ in range(h * w)]

for query in queries:
    if query[0] == 1:
        _, px, py = query
        query1(px, py)
    else:
        _, px, py, qx, qy = query
        flag = query2(px, py, qx, qy)
        if flag:
            print('Yes')
        else:
            print('No')
