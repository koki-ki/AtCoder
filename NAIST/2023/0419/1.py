n = int(input())
can = set([i for i in range(1, 2 * n + 2)])

while len(can) > 0:
    takahashi = min(can)
    print(takahashi)
    can.remove(takahashi)
    aoki = int(input())

    if aoki == 0:
        exit()
    can.remove(aoki)

