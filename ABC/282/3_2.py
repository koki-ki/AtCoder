n = int(input())
s = list(input())
num_of_d = 0
protected = [False] * n

for i, c in enumerate(s):
    if num_of_d % 2 == 1:
        protected[i] = True
    if s[i] == '"':
        num_of_d += 1
ans = ''
for i, c in enumerate(s):
    if protected[i]:
        continue
    else:
        if s[i] == ',':
            s[i] = '.'

ans = ''.join(s)
print(ans)
