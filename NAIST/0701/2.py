from math import sqrt

n = int(input())
x, y = [], []
for i in range(n):
    x_, y_ = map(int, input().split())
    x.append(x_)
    y.append(y_)

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            ab = sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            bc = sqrt((x[j] - x[k]) ** 2 + (y[j] - y[k]) ** 2)
            ca = sqrt((x[k] - x[i]) ** 2 + (y[k] - y[i]) ** 2)

            if ab + bc == ca or bc + ca == ab or ca + ab == bc:
                print('Yes')
                exit()

print('No')