s = input()
length = len(s)
ans = 1
for i in range(length - 1):
    for j in range(i + 1, length):
        if s[i:j+1] == s[i:j+1][::-1]:
            ans = max(ans, j - i + 1)

print(ans)
