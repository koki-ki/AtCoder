n, k = map(int, input().split())
ab = []
sum_ = 0
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
    sum_ += b

ab.sort(key=lambda x: x[0])

if sum_ <= k:
    print(1)
    exit()


for a, b in ab:
    sum_ -= b
    if sum_ <= k:
        print(a + 1)
        exit()