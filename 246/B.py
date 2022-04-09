import math
a, b = map(int, input().split())
x = a / math.sqrt(a ** 2 + b ** 2)
y = b / math.sqrt(a ** 2 + b ** 2)
print(x, y)

