s = input()
if len(s) % 8 != 0:
    print('No')
    exit()

try:
    if s[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and 100000 <= int(s[1: 7]) <= 999999 and s[7] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print('Yes')
    else:
        print('No')
except:
    print('No')

