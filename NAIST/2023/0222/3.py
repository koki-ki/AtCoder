from collections import defaultdict

n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

divided = [[] for _ in range(k)]
for i in range(n):
    divided[i % k].append(t[i])

ans = 0
get = {'r': p, 's': r, 'p': s}

for i, d in enumerate(divided):
    turn = len(d)
    dp = [defaultdict(int) for _ in range(turn)]
    dp[0]['r'] = get['r'] if d[0] == 'r' else 0
    dp[0]['s'] = get['s'] if d[0] == 's' else 0
    dp[0]['p'] = get['p'] if d[0] == 'p' else 0

    for j in range(1, turn):
        dp[j]['r'] = max(dp[j - 1]['s'], dp[j - 1]['p']) + get['r'] if d[j] != 'r' else 0
        dp[j]['p'] = max(dp[j - 1]['s'], dp[j - 1]['r']) + get['p'] if d[j] != 'p' else 0
        dp[j]['s'] = max(dp[j - 1]['r'], dp[j - 1]['p']) + get['s'] if d[j] != 's' else 0

    ans += max(dp[-1].values())

print(ans)

