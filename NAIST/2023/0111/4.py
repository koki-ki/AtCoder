h, w = map(int, input().split())
maze = []
for _ in range(h):
    maze.append(list(input()))

distances = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
for x in range(h - 1, -1, -1):
    for y in range(w - 1, -1, -1):
        if maze[x][y] == '#':
            continue
        distances[x][y] = max(distances[x + 1][y], distances[x][y + 1]) + 1
print(distances[0][0])