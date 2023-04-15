n = int(input())
s = input()
good = s.count('o')
bad = s.count('x')

if good >= 1 and bad == 0:
    print('Yes')
else:
    print('No')
