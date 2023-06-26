n = int(input())
s = list(input())
num_brackets = [0 for _ in range(n)]

for i, si in enumerate(s):
    if si == '(':
        num_brackets[i] = num_brackets[i - 1] + 1
    elif si == ')':
        num_brackets[i] = num_brackets[i - 1] - 1
    else:
        num_brackets[i] = num_brackets[i - 1]

ans = ''
if num_brackets[0] == 0:
    ans += s[0]

for i in range(1, n - 1):
    if num_brackets[i] == num_brackets[i + 1] == 0:
        ans += s[i + 1]
    elif num_brackets[i + 1] == 0:
        ans += s[i + 1]

if num_brackets[-1] <= 0:
    ans += s[-1]
print(*num_brackets)
print(ans)