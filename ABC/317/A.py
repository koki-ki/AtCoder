n, h, x = map(int, input().split())
p = list(map(int, input().split()))

need = x - h
for i, pi in enumerate(p):
    if pi >= need:
        print(i + 1)
        exit()
