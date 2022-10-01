n = int(input())
w = [0] + list(map(int, input().split()))

ans = 10 ** 18
for t in range(1, n):
    s1 = sum(w[1:t + 1])
    s2 = sum(w[t + 1:])
    ans = min(ans, abs(s1 - s2))
print(ans)