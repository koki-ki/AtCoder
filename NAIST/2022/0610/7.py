import math

t = int(input())

for i in range(t):
    balls = list(map(int, input().split()))
    balls.sort()
    start_b = [balls[0], balls[1], balls[2]]
    if (balls[2] - balls[0]) % 2 == 0:
        print(-1)
        continue

    hiku = math.ceil((max(balls) - min(balls)) / 2 )
    balls[0] += min(hiku, balls[1]) * 2
    balls[1] -= min(hiku, balls[1])
    balls[2] -= min(hiku, balls[1])

    if balls[0] >= balls[2]:
        ans = abs(start_b[0] - balls[0])
        print(ans)


