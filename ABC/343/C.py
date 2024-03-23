def check(s):
    s = list(str(s))
    s_reversed = list(reversed(s))
    return s == s_reversed


n = int(input())
i = 1
ans = 1

while i ** 3 <= n:
    k = i ** 3
    if check(k):
        ans = k
    i += 1

print(ans)
