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

# -- main --
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
uf = UnionFind(n)
for _ in range(m):
    c, d = map(lambda x: int(x) - 1, input().split())
    uf.unite(c, d)
sum_a = [0 for _ in range(n)]
sum_b = [0 for _ in range(n)]

for i in range(n):
    x = uf.root(i)
    sum_a[x] += a[i]
    sum_b[x] += b[i]

if sum_a == sum_b:
    print("Yes")
else:
    print("No")