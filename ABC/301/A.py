n = int(input())
s = input()

t = s.count('T')
a = s.count('A')

if t > a:
    print('T')
elif t < a:
    print('A')
elif s[-1] == 'A':
    print('T')
else:
    print('A')

