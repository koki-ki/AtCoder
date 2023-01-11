n = int(input())
p = list(map(int, input().split()))

set_ = set()
min_ = 0

for i in range(n):
    set_.add(p[i])
    while min_ not in set_:
        min_ += 1
    print(min_)
