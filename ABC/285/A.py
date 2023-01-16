a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
flag = False
if a == 1 and (b == 2 or b == 3):
    flag = True
elif a == 2 and (b == 4 or b == 5):
    flag = True
elif a == 3 and (b == 6 or b == 7):
    flag = True
elif a == 4 and (b == 8 or b == 9):
    flag = True
elif a == 5 and (b == 10 or b == 11):
    flag = True
elif a == 6 and (b == 12 or b == 13):
    flag = True
elif a == 7 and (b == 14 or b == 15):
    flag = True

if flag:
    print('Yes')
else:
    print('No')