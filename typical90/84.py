n = int(input())
s = input()
all = n * (n + 1) // 2

zipped = []
cnt = 1
i = 0
while i < n - 1:
    if s[i] != s[i + 1]:
        zipped.append(cnt)
        cnt = 1
    else:
        cnt += 1
    i += 1
zipped.append(cnt)

ans = all - sum([d * (d + 1) // 2 for d in zipped])
print(ans)

