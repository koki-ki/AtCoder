s = list(input())
index_of_xy = []
for i in range(len(s)):
    if s[i] == 'B':
        index_of_xy.append(i)

x, y = index_of_xy
if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
    condition1 = True
else:
    condition1 = False

for i in range(len(s)):
    if s[i] == 'K':
        if i == 0 or i == 7:
            condition2 = False
        elif 1 <= i <= 6 and s[i] == 'K' and 'R' in s[:i] and 'R' in s[i:]:
            condition2 = True
        else:
            condition2 = False

if condition1 and condition2:
    print('Yes')
else:
    print('No')
