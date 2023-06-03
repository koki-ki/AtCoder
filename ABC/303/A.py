n = int(input())
s = input()
t = input()

def check(x, y):
    if x == y or (x == '1' and y == 'l') or (x == '0' and y == 'o') or (x == 'l' and y == '1') or (x == 'o' and y == '0'):
        return True
    else:
        return False

flag = True

for i in range(n):
    flag = check(s[i], t[i])
    if flag is False:
        break

if flag:
    print('Yes')
else:
    print('No')