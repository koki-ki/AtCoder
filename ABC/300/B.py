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

def h_shift(a):
    new_a = []
    h = len(a)
    for i in range(h):
        new_a.append(a[i][1:] + [a[i][0]])
    return new_a

def v_shift(a):
    a = transpose(a)
    new_a = h_shift(a)
    new_a = transpose(new_a)
    return new_a

def shift(a, s, t):
    for _ in range(s):
        a = h_shift(a)
    for _ in range(t):
        a = v_shift(a)

    return a

h, w = map(int, input().split())

a = []
for _ in range(h):
    a.append(list(input()))

b = []
for _ in range(h):
    b.append(list(input()))

for i in range(w):
    for j in range(h):
        new_a = shift(a, i, j)
        if new_a == b:
            print('Yes')
            exit()


print('No')

