n = int(input())
s = list(input())

left_brackets = []
right_brackets = []
checked = [False for _ in range(n)]

for i, si in enumerate(s):
    if si == '(':
        left_brackets.append(i)
    elif si == ')':
        right_brackets.append(i)

pair_of_brackets = []
b = [0 for _ in range(n + 1)]
left_bracket = n - 1

for i, r in enumerate(right_brackets):
    for i in range(r - 1, -1, -1):
        if s[i] == '(' and not checked[i]:
            checked[i] = True
            checked[r] = True
            pair_of_brackets.append((i, r))
            b[i] += 1
            b[r + 1] -= 1
            if left_bracket == 0 and i != n - 1:
                left_bracket = r[i + 1] - 1
            break

acc = [0 for _ in range(n + 1)]
acc[0] = b[0]
for i in range(n):
    acc[i + 1] = acc[i] + b[i + 1]

# print(b)
# print(acc)

if sum(acc) == 0:
    ans = ''.join(s)
else:
    ans = ''
    for i in range(n):
        if acc[i] == 0:
            ans += s[i]

print(ans)