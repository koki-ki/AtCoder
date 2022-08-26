from multiprocessing.pool import AsyncResult


INF = 998244353
N = int(input())
keta = len(str(N))
ans = 0

def sum(x):
    return x * (x + 1) // 2

for i in range(1, keta + 1):
    # i: 桁数
    x = min(N, 10 ** i - 1) - (10 ** (i - 1) - 1)
    ans += sum(x)
    ans %= INF


print(ans)