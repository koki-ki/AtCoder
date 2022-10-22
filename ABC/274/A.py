from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

a, b = map(int, input().split())
s = Decimal(str(b / a)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
print(s)
