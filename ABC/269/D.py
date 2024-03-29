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

# main
n = int(input())
uf = UnionFind(n)

x = []
y = []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

for i in range(n):
    x1, y1 = x[i], y[i]
    for j in range(i, n):
        x2, y2 = x[j], y[j]
        if(max(abs(x1 - x2), abs(y1 - y2)) == 1) and (y1 - y2) != - (x1 - x2):
            uf.unite(i, j)

memo = set()
for i in range(n):
    r = uf.root(i)
    if r not in memo:
        memo.add(r)

print(len(memo))
