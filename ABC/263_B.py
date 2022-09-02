n = int(input())
p = [0, 0] + list(map(int, input().split()))
cnt = 0
now = n
while now != 1:
    cnt += 1
    now = p[now]
print(cnt)
