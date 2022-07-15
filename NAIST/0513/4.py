import math
n = int(input())
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)
a = 1
for i in range(2, n + 1):
    a = my_lcm(a, i)

print(a + 1)