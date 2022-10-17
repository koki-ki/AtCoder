from decimal import Decimal, ROUND_HALF_UP
x, k = map(int, input().split())
for i in range(k):
    x = int(Decimal(x).quantize(Decimal('1E'+str(i + 1)), rounding=ROUND_HALF_UP))

print(x)
