n = int(input())
a = list(map(int, input().split()))

distance = [0 for _ in range(2 * n + 2)]
for i, ai in enumerate(a, start=1):
    distance[i * 2] = distance[ai] + 1
    distance[i * 2 + 1] = distance[ai] + 1

for d in distance[1:]:
    print(d)