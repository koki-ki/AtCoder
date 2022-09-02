h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(input())
new_a = []
for i in range(h):
    if a[i].count('#') != 0:
        new_a.append(a[i])
a = new_a
a = [list(x) for x in zip(*a)]

new_a = []


for i in range(w):
    if a[i].count('#') != 0:
        new_a.append(a[i])
a = new_a
a = [list(x) for x in zip(*a)]

for i in range(len(a)):
    print(''.join(a[i]))
