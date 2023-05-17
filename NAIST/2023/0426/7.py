def d(n):
    return len(str(n))

def buy(n):
    return a * n + b * d(n)

a, b, x = map(int, input().split())
ans = 0

low = 0
high = 10 ** 9 + 1

while high - low > 1:
    middle = (low + high) // 2
    if x >= buy(middle):
        low = middle
    else:
        high = middle

print(low)
