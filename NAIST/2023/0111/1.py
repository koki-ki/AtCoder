n = int(input())
s = []
t = []
for _ in range(n):
    s_, t_ = input().split()
    s.append(s_)
    t.append(t_)

for i in range(n):
    for j in range(n):
        if i == j: continue
        if s[i] == s[j] and t[i] == t[j]:
            print('Yes')
            exit()

print('No')