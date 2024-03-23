class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1 for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]

    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] >= self.size[rootv]:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]
            else:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]

    def same(self, u, v):
        return self.root(u) == self.root(v)


n, q = map(int, input().split())
uf = UnionFind(n)

for _ in range(q):
    query = input().split()
    if query[0] == "1":
        u, v = map(int, query[1:])
        uf.unite(u, v)
    else:
        u, v = map(int, query[1:])
        if uf.same(u, v):
            print("Yes")
        else:
            print("No")
