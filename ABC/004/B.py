c = []
for _ in range(4):
    c.append(list(input().split()))

for i in range(4):
    print(*c[-(i + 1)][::-1])
