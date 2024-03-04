n = int(input())
s = input()

x = 0
y = 0

passed = set()
passed.add((0, 0))
for i in range(n):
    if s[i] == "R":
        x += 1
    elif s[i] == "D":
        y -= 1
    elif s[i] == "L":
        x -= 1
    else:
        y += 1
    if (x, y) in passed:
        print("Yes")
        exit()
    else:
        passed.add((x, y))
print("No")