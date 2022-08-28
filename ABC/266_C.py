a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))


def isInside(a, b, c, d):
    abXad = (b[0] - a[0]) * (d[1] - a[1]) - (b[1] - a[1]) * (d[0] - a[0])
    bcXbd = (c[0] - b[0]) * (d[1] - b[1]) - (c[1] - b[1]) * (d[0] - b[0])
    caXcd = (a[0] - c[0]) * (d[1] - c[1]) - (a[1] - c[1]) * (d[0] - c[0])

    if (abXad > 0. and bcXbd > 0. and caXcd > 0.) or (abXad < 0. and bcXbd < 0. and caXcd < 0.):
        return True
    elif abXad * bcXbd * caXcd == 0:
        return False

    return False


def isConcave(px, py):
    for i in range(4):
        if isInside([px[i % 4], py[i % 4]], [px[(i+1) % 4], py[(i+1) % 4]], [px[(i+2) % 4], py[(i+2) % 4]], [px[(i+3) % 4], py[(i+3) % 4]]):
            return True

    return False


xs = [a[0], b[0], c[0], d[0]]
ys = [a[1], b[1], c[1], d[1]]
if isConcave(xs, ys):
    print('No')
else:
    print('Yes')
