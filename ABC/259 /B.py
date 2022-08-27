import math
a, b, d = map(int, input().split())
theta = math.radians(d)
a_ = a * math.cos(theta) - b * math.sin(theta)
b_ = a * math.sin(theta) + b * math.cos(theta)
print(a_, b_)
