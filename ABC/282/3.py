n = int(input())
s = input()

doubles = []
ans = ''

for i, c in enumerate(s):
    if c == '"':
        doubles.append(i)
cnt = 0
i = 0
# print(doubles)
while i < len(s):
    # print(ans, i, cnt)
    if cnt <= len(doubles) // 2:
        if i == doubles[cnt]:
            ans += s[doubles[cnt]: doubles[cnt + 1] + 1]
            i += doubles[cnt + 1] - doubles[cnt] + 1
            cnt += 2
        else:
            if s[i] == ',':
                ans += '.'
            else:
                ans += s[i]
            i += 1
            if i >= len(s):
                break
    else:
        if s[i] == ',':
            ans += '.'
        else:
            ans += s[i]
        i += 1
        if i >= len(s):
            break


print(ans)
