n, x = map(int, input().split())
a = list(map(int, input().split()))

now = sum(a) - min(a) - max(a)

for i in range(0, 101):
    tmp = now
    if i <= min(a):
        tmp += min(a)
    elif min(a) <= i <= max(a):
        tmp += i
    else:
        tmp += max(a)
    if tmp >= x:
        print(i)
        exit()

print(-1)
