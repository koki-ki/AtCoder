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

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.unite(a, b)

ans = max(uf.size)
print(ans)