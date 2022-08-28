n = int(input())
s = {}
for i in range(n):
    s_ = input()
    if s_ not in s.keys():
        s[s_] = 1
        print(s_)
    else:
        print(s_ + '(' +  str(s[s_]) + ')')
        s[s_] += 1


