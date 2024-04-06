from collections import defaultdict

INF = 10 ** 18

n = int(input())
color_min_value = defaultdict(lambda: INF)

for _ in range(n):
    a, c = map(int, input().split())
    color_min_value[c] = min(color_min_value[c], a)

ans = max(color_min_value.values())
print(ans)
