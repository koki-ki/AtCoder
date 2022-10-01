n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_ = max(a)
suki = []

for i in range(n):
    if a[i] == max_:
        suki.append(i + 1)

for i in range(k):
    if b[i] in suki:
        print('Yes')
        exit()

print('No')


