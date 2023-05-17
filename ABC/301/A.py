n = int(input())
s = input()
t = s.count('T')
a = s.count('A')

if a > t:
    print('A')
elif a < t:
    print('T')
else:
    cnt = {}
    cnt['A'] = 0
    cnt['T'] = 0
    for s_ in list(s):
        cnt[s_] += 1
        if cnt[s_] == t and s_ == 'T':
            print('T')
            exit()
        elif cnt[s_] == a and s_ == 'A':
            print('A')
            exit()