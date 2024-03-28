n = int(input())
d = [0] + list(map(int, input().split()))

ans = 0

for month in range(1, n + 1):
    for day in range(1, d[month] + 1):
        day = str(month) + str(day)
        if len(set(day)) == 1:
            ans += 1

print(ans)
