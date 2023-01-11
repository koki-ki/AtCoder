s = input()

def check(s):
    if s[:len(s)//2] == s[len(s)//2:]:
        return True
    else:
        return False

ans = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if check(s[i:j]):
            ans = max(ans, j - i)

print(ans)

