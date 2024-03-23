n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

candidates = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            candidates.add(a[i] + b[j] + c[k])

for xi in x:
    if xi in candidates:
        print("Yes")
    else:
        print("No")
