n = int(input())
s, t = [], []

for i in range(n):
    S, T = input().split()
    s.append(S)
    t.append(int(T))

original = set()
original_num = list()

for i in range(n):
    if not(s[i] in original):
        original.add(s[i])
        original_num.append(i)

tmp = t[i]
ans = 0
max_ = t[0]

for i in range(len(original_num)):
    if max_ < t[original_num[i]]:
        max_ = t[original_num[i]]
        ans = original_num[i]

ans += 1
print(ans)


