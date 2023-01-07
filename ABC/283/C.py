s = input()
cnt = 0
i = 0
while i < len(s) - 1:
    if s[i] == s[i + 1] == '0':
        cnt += 1
        i += 2
        continue
    i += 1

ans = len(s) - cnt
print(ans)
