n = int(input())
s = ' ' + input()

for i in range(1, n):
    ans = 0
    check = [False] * (n - i + 1)
    for k in range(1, n - i + 1):
        if s[k] != s[k + i]:
            check[k] = True
    for l in range(1, n - i + 1):
        if check[l]:
            ans = l
        else:
            break
    print(ans)
