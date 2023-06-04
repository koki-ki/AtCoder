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

def distance_squared(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

# main
n, d = map(int, input().split())
x = []
y = []

for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

uf = UnionFind(n)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x1, y1, x2, y2 = x[i], y[i], x[j], y[j]
        if distance_squared(x1, y1, x2, y2) <= d ** 2:
            uf.unite(i, j)

for i in range(n):
    if uf.same(0, i):
        print('Yes')
    else:
        print('No')
