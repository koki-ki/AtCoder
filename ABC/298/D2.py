from collections import deque
q = int(input())
s = deque(['1'])
n = 1
keta = 1
MOD = 998244353

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x = query
        keta += 1
        s.append(str(x))
        n = (n * 10 + x) % MOD

    elif query[0] == 2:
        top = s.popleft()
        keta -= 1
        top = int(top)

        n = n - (top * pow(10, keta, MOD))
        n %= MOD

    else:
        ans = n % MOD
        print(ans)