n, m = map(int, input().split())
num = ['0'] * n
keta = [0] * n

for _ in range(m):
    s, c = map(int, input().split())
    s -= 1
    if keta[s] == 1:
        if num[s] == str(c):
            continue
        else:
            print(-1)
            exit()
    keta[s] = 1
    num[s] = str(c)
# print(num)

ans = ''.join(num)
ans = int(ans)

if len(str(ans)) < n:
    print(-1)
    exit()

print(ans)
