s = input()
a, b, c = s[0], s[1], s[2]
if s.count(a) == 1:
    print(a)
elif s.count(b) == 1:
    print(b)
elif s.count(c) == 1:
    print(c)
else:
    print(-1)