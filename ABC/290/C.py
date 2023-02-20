n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(set(a))

m = 0
cnt = 0
for i in range(len(a)):
    if a[i] == m:
        m += 1
        cnt += 1
    elif a[i] != m:
        break
    if cnt == k:
        break

print(m)