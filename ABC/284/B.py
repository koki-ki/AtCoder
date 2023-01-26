t = int(input())
anses = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = [i % 2 for i in a]
    anses.append(a.count(1))

for ans in anses:
    print(ans)
