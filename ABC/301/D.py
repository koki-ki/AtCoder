s = input()
n = int(input())

length = len(s)

l = r = 0

for i in range(length):
    if s[-(i + 1)] == '?':
        r += 2 ** i
    elif s[-i] == '1':
        l += 1
        r += 1

m = (l + r) // 2 if l != r else -1
if m == -1:
    print(-1)
    exit()

while l != r:
    if m <= n:
        r = m
        m = (l + r) // 2
    else:
        l = m + 1
        m = (l + r) // 2


print(m)


