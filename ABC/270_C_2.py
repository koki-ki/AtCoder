n, x, y = map(int, input().split())
x -= 1
y -= 1
A = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    A[u].append(v)
    A[v].append(u)

seen = [x]
todo = [A[x]]

print('todo', todo)
while todo != []:
    thistime = todo.pop(-1)
    print(thistime)
    cnt = 0
    for i in thistime:
        cnt += 1
        if i in seen:
            for _ in range(cnt):
                seen.pop(-1)
                continue
        seen.append(i)
        todo.append(i)


print(*seen)
