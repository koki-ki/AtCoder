s = input()
char = []
oomoji = False
komoji = False

for i in range(len(s)):
    if s[i] in char:
        print('No')
        exit()
    if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        oomoji = True
    if s[i] in 'abcdefghijklmnopqrstuvwxyz':
        komoji = True
    char.append(s[i])

if oomoji and komoji:
    print('Yes')
else:
    print('No')

