def solve(m):
    cnt = 0
    pre = 0
    for i in range(1, n + 1):
        if a[i] - pre >= m and l - a[i] >= m:
            cnt += 1
            pre = a[i]
    if cnt >= k:
        return True
    return False

# -- main --
n, l = map(int, input().split())
k = int(input())
a = [0] + list(map(int, input().split()))

left = -1
right = l + 1

while (right - left > 1):
    mid = left + (right - left) // 2
    if not solve(mid):
        right = mid
    else:
        left = mid

print(left)