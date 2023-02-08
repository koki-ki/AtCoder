N, M = map(int, input().split())
S = []
T = []

for _ in range(N):
    s = input()
    S.append(s)

for _ in range(M):
    t = input()
    T.append(t)

ans = 0

for s in S:
    for t in T:
        if s[-3:] == t:
            ans += 1
            break

print(ans)