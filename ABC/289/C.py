n, m = map(int, input().split())
s = []
for _ in range(m):
    c = int(input())
    s.append(list(map(int, input().split())))
ans = 0

for i in range(1 << (m + 1)):
    exist = [False for _ in range(n + 1)]
    exist[0] = True
    flag = True
    for j in range(m):
        if i & 1 << j:
            for k in s[j]:
                exist[k] = True
    for j in range(n + 1):
        if not exist[j]:
            flag = False
            break
    if flag:
        ans += 1
print(ans // 2)



