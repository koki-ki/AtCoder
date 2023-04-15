q = int(input())
s = 1
MOD = 998244353

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x = query
        s = str(s)
        s = s + str(x)
    elif query[0] == 2:
        num_keta = len(str(s))
        s = int(s)
        s %= 10 ** (num_keta - 1)
    else:
        s = int(s)
        ans = s % (MOD * MOD) % MOD
        print(ans)