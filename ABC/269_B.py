s = []
for _ in range(10):
    s.append(list(input()))

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                stmp = [['.' for _ in range(10)] for _ in range(10)]
                for i in range(10):
                    for j in range(10):
                        if a <= i <= b and c <= j <= d:
                            stmp[i][j] = '#'
                # if (a, b, c, d) == (5, 8, 4, 9):
                #     for k in range(10):
                #         print(stmp[k])
                if stmp == s:
                    # print('Success')
                    # if (a, b, c, d) == (5, 8, 4, 9):
                    #     for k in range(10):
                    #         print(stmp[k])
                    print(a + 1, b + 1)
                    print(c + 1, d + 1)
