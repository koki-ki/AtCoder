from itertools import permutations

n, k = map(int, input().split())
t = []
for _ in range(n):
    t.append(list(map(int, input().split())))

ans = 0

paths = list(permutations(range(1, n), n - 1))

for path in paths:
    time = 0
    time += t[0][path[0]]
    for i in range(n - 2):
        time += t[path[i%n]][path[(i + 1) % n]]
    time += t[path[-1]][0]
    if time == k:
        ans += 1

print(ans)
