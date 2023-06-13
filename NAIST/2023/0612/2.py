def check(a):
    n = len(a)
    for i in range(n):
        if a[i] != a[n - 1- i]:
            return False
    return True


s = input()
rs = s[::-1]
ans = 0
n = len(s)

l_num_a = 0
r_num_a = 0
for i in range(n - 1):
    if s[i:i+1] == 'aa':
        l_num_a += 1
    else:
        break


if check(s):
    print('Yes')
    exit()

for i in range(n - 1):
    if rs[i] == 'a':
        r_num_a += 1
    else:
        break

if l_num_a != r_num_a:
    print('No')
    exit()

if s[:r_num_a] == ''.join(list(reversed(s[:r_num_a:]))):
    print('Yes')

