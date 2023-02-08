import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
ans = 1 << 60

for ai in a:
    left = bisect.bisect_left(b, ai)
    right = bisect.bisect_right(b, ai)
    ans = min(ans, abs(ai - b[left]), abs(ai - b[right]))

print(ans)
