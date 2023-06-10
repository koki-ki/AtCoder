p, q = input().split()
dist = {'A': 0, 'B': 3, 'C': 4, 'D': 8, 'E': 9, 'F': 14, 'G': 23}
px = dist[p]
py = dist[q]

ans = abs(px - py)
print(ans)


