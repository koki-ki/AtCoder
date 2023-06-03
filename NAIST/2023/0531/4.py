n, x = map(int, input().split())
a = set(map(int, input().split()))

flag = False
for ai in a:
    aj = ai - x
    if aj in a:
        flag = True
        break

if flag:
    print('Yes')
else:
    print('No')
