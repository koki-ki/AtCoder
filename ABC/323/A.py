s = input()
flag = True
for i in range(1, 16, 2):
    if s[i] != "0":
        flag = False


ans = "Yes" if flag else "No"
print(ans)
