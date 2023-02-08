n = int(input())
s = list(input())

ans = 0
for num in range(1000):
    now = 0
    cipher = '0' * (3 - len(str(num))) + str(num)
    f1 = False
    f2 = False
    f3 = False
    for i in range(n - 2):
        if s[i] == cipher[0]:
            now = i + 1
            f1 = True
            break
    for i in range(now, n - 1):
        if s[i] == cipher[1]:
            now = i + 1
            f2 = True
            break
    for i in range(now, n):
        if s[i] == cipher[2]:
            f3 = True
            break
    if f1 and f2 and f3:
        ans += 1
print(ans)