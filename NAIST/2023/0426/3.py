import bisect

INF = 10 ** 10

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = INF

B.sort()

for a in A:
    ind_a = bisect.bisect_left(B, a)
    if ind_a == 0:
        ans = min(ans, abs(a - B[0]))
    elif ind_a == m:
        ans = min(ans, abs(a - B[m - 1]))
    else:
        ind_a -= 1
        ind_a_next = ind_a + 1
        ans = min(ans, abs(a - B[ind_a]), abs(a - B[ind_a_next]))

print(ans)