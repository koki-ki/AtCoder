n = int(input())
a = list(map(int, input().split()))

syl = []
sum = 0

for i in range(n):
    # print('syl:', syl)
    # print('sum:', sum)
    if len(syl) == 0:
        syl.append([a[i], 1])
        sum += 1
        print(sum)
        continue

    if syl[-1][0] != a[i]:
        syl.append([a[i], 1])

    else:
        syl[-1][1] += 1

    sum += 1

    if syl[-1][0] == a[i] and syl[-1][1] == a[i]:
        syl.pop(-1)
        sum -= a[i]

    print(sum)



