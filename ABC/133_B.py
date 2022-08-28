import math

n, d = map(int, input().split())
x = []
for i in range(n):
    x_ = list(map(int, input().split()))
    x.append(x_)

def check(x, y):
    '''xとyの距離の平方根をとってint(dist_)-dist_==0だったらTrue'''
    dist_ = 0
    for i in range(len(x)):
        dist_ += (x[i] - y[i]) ** 2
    dist_ = math.sqrt(dist_)
    if int(dist_) - dist_ == 0: return True
    else: return False

cnt = 0
for i in range(n - 1):
    for j in range(i, n):
        if i == j:
            continue

        if check(x[i], x[j]): cnt += 1

print(cnt)
