h, w = map(int, input().split())
c = []
for _ in range(h):
    c.append(list(input()))
x = [0] * w
for w_ in range(w):
    for h_ in range(h):
        x[w_] += 1 if c[h_][w_] == '#' else 0
print(*x)
