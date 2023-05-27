n = int(input())
s = list(input())

t = []

for i in range(n):
    t.append(s[i])
    if 3 <= len(s) and t[-3:] == ['f', 'o', 'x']:
        t.pop()
        t.pop()
        t.pop()

print(len(t))