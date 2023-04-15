s = []
for _ in range(8):
    s.append(input())

row = [i for i in range(1, 9)]
col = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            print(col[j] + str((9 - row[i])))