n, k, a = map(int, input().split())
ans = (a + k - 1) % n
if ans == 0:
    ans = n
print(ans)