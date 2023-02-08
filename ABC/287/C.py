import sys
sys.setrecursionlimit(10 ** 6)
# class UnionFind
class unionfind:
	# n 頂点の Union-Find 木を作成
	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1) # 最初は親が無い
		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1

	# 頂点 x の根を返す関数
	def root(self, x):
		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
		while self.par[x] != -1:
			x = self.par[x]
		return x

	# 要素 u, v を統合する関数
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			# u と v が異なるグループのときのみ処理を行う
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]

	#  要素 u と v が同一のグループかどうかを返す関数
	def same(self, u, v):
		return self.root(u) == self.root(v)
# dfs
def dfs(v, G, seen):
    global is_closed
    seen[v] = True
    for v2 in G[v]:
        if seen[v2]:
            is_closed = True
            continue
        dfs(v2, G, seen)
    return

# main
n, m = map(int, input().split())
uf = unionfind(n)

G = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if uf.same(u, v):
        print('No')
        exit()
    G[u].append(v)
    G[v].append(u)
    uf.unite(u, v)

for v in G:
    if len(v) >= 3:
        print('No')
        exit()

# dfs
seen = [False for _ in range(n)]
num_of_con = 0

for v in range(n):
    if seen[v]:
        continue

    dfs(v, G, seen)
    num_of_con += 1

if num_of_con == 1:
    print('Yes')
else:
    print('No')