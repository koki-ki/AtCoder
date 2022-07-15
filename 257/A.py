n, x = map(int, input().split())

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = ''
for i in range(26):
    a += alpha[i] * n

print(a[x - 1])