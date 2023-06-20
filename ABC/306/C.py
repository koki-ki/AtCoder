def f(a):
    indices = [[] for _ in range(n + 1)]

    for i, ai in enumerate(a):
        indices[ai].append(i + 1)

    for index in indices:
        index.sort()

    center_indices = [[0, i] for i in range(n + 1)]
    for i, index in enumerate(indices[1:], 1):
        center_indices[i][0] = index[1]

    return center_indices

n = int(input())
a = list(map(int, input().split()))

indices = f(a)
indices = sorted(indices, key=lambda x: x[0])

ans = []

for index in indices[1:]:
    ans.append(index[1])

print(*ans)



