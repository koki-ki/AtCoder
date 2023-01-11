n = int(input())
BIG = 10 ** 9 + 7
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factors = {}
for i in range(1, n + 1):
    factors_ = factorization(i)
    for f in factors_:
        if f[0] not in factors:
            factors[f[0]] = 1
        else:
            factors[f[0]] += f[1]

ans = 1
kakeru = list(factors.values())
for k in kakeru[1:]:
    ans *= (k + 1)
    ans %= BIG

print(ans)

