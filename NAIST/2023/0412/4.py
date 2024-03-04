n, p = map(int, input().split())
a = list(map(int, input().split()))
ans = sum([1 for ai in a if ai < p])
print(ans)
