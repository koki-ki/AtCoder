n, m = map(int, input().split())
s = input()
t = input()

f1, f2 = False, False

if s == t[:n]:
    f1 = True
if s == t[-n:]:
    f2 = True

if f1 and f2:
    print(0)
elif f1:
    print(1)
elif f2:
    print(2)
else:
    print(3)
