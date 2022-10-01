n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))
b = [0] * (n + 1)
b[1] = 1

i = 1
cnt = 0
while True:

    if b[a[i]] == 1:
        print(-1)
        exit()
    i = a[i]
    b[i] = 1
    cnt += 1
    if b[2] == 1:
        break

print(cnt)



