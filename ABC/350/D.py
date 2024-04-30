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
    uf.unite(a - 1, b - 1)

ans = 0
checked = set()
for i in range(n):
    if uf.root(i) not in checked:
        j = uf.size[uf.root(i)]
        ans += j * (j - 1) // 2
        checked.add(uf.root(i))
ans -= m
print(ans)
