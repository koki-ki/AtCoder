import copy
r, c = map(int, input().split())
b = []

for _ in range(r):
    b.append(list(input()))
new_b = copy.deepcopy(b)
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(r):
    for j in range(c):
        if b[i][j] in numbers:
            dist = int(b[i][j])
            for x in range(r):
                for y in range(c):
                    if abs(x - i) + abs(y - j) <= dist:
                        new_b[x][y] = '.'

for i in range(r):
    print(''.join(new_b[i]))