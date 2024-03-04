n = int(input())
s = []
p = []

for _ in range(n):
    s_, p_ = input().split()
    p_ = int(p_)
    s.append(s_)
    p.append(p_)

sum_population = sum(p)
for i, p_ in enumerate(p):
    if p_ > sum_population // 2:
        print(s[i])
        exit()

print("atcoder")
