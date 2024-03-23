s = input()
n = len(s)
for i in range(n):
    if i == 0 and not (s[i] == "<"):
        print("No")
        exit()
    elif 1 <= i <= n - 2 and not (s[i] == "="):
        print("No")
        exit()
    elif i == n - 1 and not (s[i] == ">"):
        print("No")
        exit()
print("Yes")
