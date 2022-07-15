import math

x, y = map(int, input().split())

def is_prime(n):
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if x == y:
    print(-1)
    exit()

x_p = prime_factorize(x)
y_p = prime_factorize(y)



kesu = []
for i in range(len(y_p)):
    if y_p[i] in x_p:
        x_p.remove(y_p[i])
        kesu.append(y_p[i])

for i in range(len(kesu)):
    y_p.remove(kesu[i])

p = 2
while x * p < 10 ** 9:
    if p in y_p:
        p += 1
        continue
    if y % (x * p) != 0:
        print(x * p)
        exit()

print(-1)