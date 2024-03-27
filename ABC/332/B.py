k, g, m = map(int, input().split())
glass = 0
cup = 0

for _ in range(k):
    if glass == g:
        glass = 0
    elif cup == 0:
        cup = m
    else:
        tmp = g - glass
        if tmp >= cup:
            glass += cup
            cup = 0
        else:
            glass += tmp
            cup -= tmp

print(glass, cup)
