n = int(input())

zeros = []
ones = []

i = 1
cnt = 0
vals = [-1 for _ in range(n + 1)]

while cnt < 20:
    print('?', i)

    si = int(input())
    cnt += 1
    vals[i] = si

    if si == 0:
        zeros.append(i)
        i += 2
    else:
        ones.append(i)
        if len(zeros) != 0:
            continue
        else:
            break

