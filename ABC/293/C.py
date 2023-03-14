from itertools import combinations
h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(list(map(int, input().split())))
# ways = ["r"] * (w - 1) + ["d"] * (h - 1)

downs = combinations(list(range(h + w - 2)), h - 1)

ans = 0
for down in downs:
    x = 0
    y = 0
    encounteredNums = set()
    encounteredNums.add(a[0][0])
    for i in range(h + w - 2):
        if i in down:
            x += 1
        else:
            y += 1
        encounteredNums.add(a[x][y])
    # print(encounteredNums)

    if len(encounteredNums) == h + w - 1:
        ans += 1
print(ans)
