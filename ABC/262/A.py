y = int(input())
if y % 4 == 2:
    ans = y
elif y % 4 == 0:
    ans = y + 2
elif y % 4 == 1:
    ans = y + 1
elif y % 4 == 3:
    ans = y + 3
print(ans)