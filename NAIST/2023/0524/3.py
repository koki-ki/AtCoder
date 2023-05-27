s = input()
length = len(s)

d = list()

for i in range(length):
    d.append(s[i:] + s[:i])

d.sort()
print(d[0])
print(d[-1])