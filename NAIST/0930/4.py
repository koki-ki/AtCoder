from math import sqrt
n = int(input())
x = list(map(int, input().split()))


def man(x):
    x = list(map(abs, x))
    return sum(x)


def square(x):
    return x ** 2


def euc(x):
    x = list(map(square, x))
    return sqrt(sum(x))


def che(x):
    x = list(map(abs, x))
    return max(x)


print(man(x))
print(euc(x))
print(che(x))
