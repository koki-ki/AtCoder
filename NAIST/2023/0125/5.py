q = int(input())
l = []
r = []
for _ in range(q):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

is_prime = [True] * (10 ** 5 + 1)
is_prime[0], is_prime[1] = False, False

like2017 = [False] * (10 ** 5 + 1)
cum = [0] * (10 ** 5 + 1)

for i in range(2, 10 ** 5):
    if not(is_prime[i]):
        continue
    j = 2
    while i * j <= 10 ** 5:
        is_prime[i * j] = False
        j += 1

for i in range(2, 10 ** 5 + 1):
    if is_prime[i] and is_prime[(i + 1) // 2] and (i + 1) % 2 == 0:
        like2017[i] = True

for i in range(10 ** 5):
    cum[i + 1] = cum[i] + like2017[i + 1]

for i in range(q):
    print(cum[r[i]] - cum[l[i] - 1])
