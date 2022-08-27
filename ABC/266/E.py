n = int(input())
# avgs = [0, 3.5]
if n == 1:
    print(3.5)
    exit()
avg = 4.25
avgs = [3.5, 4.25]
for i in range(2, n):
    if avg > 5:
        avg = avg * (5 / 6) + 1
    elif avg > 4:
        avg = avg * (4 / 6) + 11 / 6
        # print(avg)
    avgs.append(avg)
print(avgs[-1])
