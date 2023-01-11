n, q = map(int, input().split())
s = input()
look = 0
ans = []

for _ in range(q):
    num, x = map(int, input().split())
    if num == 1:
        look -= x
        look %= len(s)
    if num == 2:
        a = s[(look + x - 1) % len(s)]
        ans.append(a)

for a in ans:
    print(a)