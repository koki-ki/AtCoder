h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(list(map(int, input().split())))

b = [[0 for _ in range(h)] for _ in range(w)]
for i in range(w):
    for j in range(h):
        b[i][j] = a[j][i]

for i in range(w):
    print(*b[i])

def transpose(a):
    """転置行列を求める

    Args:
        a (list): h行w列の行列
    """
    h = len(a)
    w = len(a[0])

    b = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(w):
        for j in range(h):
            b[i][j] = a[j][i]