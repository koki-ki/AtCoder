N = int(input())
painted_area = set()

for _ in range(N):
    a, b, c, d = map(int, input().split())
    for x in range(a, b):
        for y in range(c, d):
            painted_area.add((x, y))

s = len(painted_area)
print(s)

