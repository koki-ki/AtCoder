s = input()
t = input()
flag = False
n = len(s)
for i in range(n):
    numMatched = 0
    for j in range(i, i + n):
        if s[(i + j) % n] == t[j % n]:
            numMatched += 1
        else:
            break
    if numMatched == n:
        flag = True
        break
if flag:
    print("Yes")
else:
    print("No")