n, x = map(int, input().split())
p = [0] + list(map(int, input().split()))
for k in range(1, n + 1):
    if p[k] == x:
        print(k)
