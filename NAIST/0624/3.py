n, l = map(int, input().split())
s = list()
for i in range(n):
    s.append(input())

s = sorted(s)
a = ''.join(s)
print(a)

