n = int(input())
s = []
a = []

for _ in range(n):
    si, ai = input().split()
    ai = int(ai)
    s.append(si)
    a.append(ai)

minage = min(a)
for i in range(n):
    if a[i] == minage:
        start = i
s = s + s
cnt = 0
for i in range(start, start + n):
    print(s[i])