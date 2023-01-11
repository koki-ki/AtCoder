n = int(input())
p = list(map(int, input().split()))
sorted_ = list(range(1, n + 1))
cnt = 0
for i in range(n):
    if p[i] != sorted_[i]:
        cnt += 1
if cnt == 2 or cnt == 0:
    print('YES')
else:
    print('NO')
