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

    return b

h, w, k = map(int, input().split())
c = []
for _ in range(h):
    c.append(input())

col = [0 for _ in range(w)]
row = [0 for _ in range(h)]

sum_black = 0
for i in range(h):
    sum_black += c[i].count("#")
    row[i] = c[i].count("#")

transposed_c = transpose(c)
for i in range(w):
    col[i] += transposed_c.count("#")

for i in range(2 ** h):
    for j in range(2 ** w):
