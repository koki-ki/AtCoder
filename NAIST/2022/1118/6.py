a, b, x = map(int, input().split())


def d(x):
    return len(str(x))


def price(n):
    return a * n + b * d(n)


def check(x):
    p = price(x)
