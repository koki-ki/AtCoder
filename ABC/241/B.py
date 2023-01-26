import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
used = [False for _ in range(len(a))]

success = True
for i in range(m):
    found = False

    for j in range(n):
        if a[j] == b[i] and (not(used[j])):
            used[j] = True
            found = True
            break

    if (not(found)):
        success = False

if success:
    print('Yes')
else:
    print('No')
