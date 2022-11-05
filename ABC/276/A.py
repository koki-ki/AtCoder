s = input()
last = -1
for i, c in enumerate(list(s)):
    if c == 'a':
        last = i + 1
print(last)
