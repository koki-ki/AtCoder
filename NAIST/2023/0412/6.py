a, b = map(int, input().split())
s = input()
flag = True

for i in range(a + b + 1):
    if i == a:
        if s[i] != '-':
            flag = False
    else:
        if s[i] not in list('0123456789'):
            flag = False

if flag:
    print("Yes")
else:
    print("No")
