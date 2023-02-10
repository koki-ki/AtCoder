MOD = 1000000007
def binpower(a, b):
    ans = 1
    while b != 0:
        if b % 2 == 1:
            ans = ans * a % MOD
        a = a * a % MOD
        b /= 2
    return ans

# input
n, k = map(int, input().split())
# main
if k == 1:
    print(1 if n == 1 else 0)
elif n == 1:
    print(k % MOD)
elif n == 2:
    print(k * (k - 1) % MOD)
else:
    print(k * (k - 1) % MOD * binpower(k - 2, n - 2) % MOD % MOD)