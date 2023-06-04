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
u = []
v = []
uf = UnionFind(n)

for _ in range(m):
    ui, vi = map(int, input().split())
    ui -= 1
    vi -= 1
    uf.unite(ui, vi)

k = int(input())
x = []
y = []
prohibited_set = set()
prohibited_list = list()

for _ in range(k):
    xi, yi = map(int, input().split())
    xi -= 1
    yi -= 1
    x.append(xi)
    y.append(yi)

    xi_root = uf.root(xi)
    yi_root = uf.root(yi)
    small_node = min(xi_root, yi_root)
    large_node = max(xi_root, yi_root)

    prohibited_set.add((small_node, large_node))
    prohibited_list.append((small_node, large_node))

Q = int(input())
ans = []
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    p_root = uf.root(p)
    q_root = uf.root(q)

    small_node = min(p_root, q_root)
    large_node = max(p_root, q_root)
    if (small_node, large_node) in prohibited_set:
        ans.append('No')
    else:
        ans.append('Yes')

for a in ans:
    print(a)
