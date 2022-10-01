k = int(input())
if k <= 59:
    ans = str(k)
    if len(ans) == 1:
        ans = '21:0' + ans
    else:
        ans = '21:' + ans
else:
    ans = str(k - 60)
    if len(ans) == 1:
        ans = '22:0' + ans
    else:
        ans = '22:' + ans
print(ans)