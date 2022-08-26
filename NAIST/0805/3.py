from multiprocessing.pool import AsyncResult


INF = 998244353
N = int(input())
keta = len(str(N))
ans = 0

if keta == 1:
    ans += N * (N + 1) // 2
    print(ans)
    exit()

# elif keta >= 2:
#     for i in range(1, keta + 1):
#         ans += (i * (i + 1) // 2) * (10 ** (i - 1))
#         ans %= INF

for i in range(1, keta):
    ans += (9 * (9 + 1) // 2) * (10 ** (i - 1))
    ans %= INF

nokori = N - int('9' * (len(str(N)) - 1))

print(ans)