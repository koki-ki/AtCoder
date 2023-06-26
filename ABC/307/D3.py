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

if n == 1:
    print(s[0])
    exit()

if num_brackets[0] <= 0:
    ans += s[0]

for i in range(1, n - 1):
    if num_brackets[i] <= 0  and not(num_brackets[i - 1] == 1 and num_brackets[i] == 0):
        ans += s[i]
        # print(1, s[i])
    elif num_brackets[i - 1] != 1 and num_brackets[i] ==0 and num_brackets[i + 1] == 1:
        ans += s[i]
        # print(2, s[i])
if num_brackets[-1] <= 1 and n >= 3:
    ans += s[-1]

print(ans)