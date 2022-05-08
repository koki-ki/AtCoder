q = int(input())
cyl = []
ans = 0
nokori = 0

for i in range(q):
    INPUT = list(input().split())
    if len(INPUT) == 3:
        _, x, c = INPUT[0], int(INPUT[1]),  int(INPUT[2])

    else:
        _, c = INPUT[0], int(INPUT[1])
        if len(cyl) == 0:
            continue
        ans = sum(cyl[:c])
        cyl = cyl[c:]
        print(ans)
        ans = 0

