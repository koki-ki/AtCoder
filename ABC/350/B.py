n, q = map(int, input().split())
teeth = [True for _ in range(n)]
t = list(map(int, input().split()))

for ti in t:
    teeth[ti-1] = not (teeth[ti-1])

ans = teeth.count(True)
print(ans)
