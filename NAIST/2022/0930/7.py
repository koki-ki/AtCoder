a, b, x = map(int, input().split())
first = a + x - a % x
if a % x == 0:
    first = a
if not(a <= first <= b):
    print(0)
    exit()

ans = 1
ans += (b - first) // x
print(ans)
