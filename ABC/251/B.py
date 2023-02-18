import itertools
n, w = map(int, input().split())
a = list(map(int, input().split()))

num = [False for _ in range(w + 1)]
check_list = []
check_list.append(list(itertools.combinations(a, 1)))
check_list.append(list(itertools.combinations(a, 2)))
check_list.append(list(itertools.combinations(a, 3)))

for c in check_list:
    for cc in c:
        sum_w = sum(cc)
        if sum_w <= w:
            num[sum(cc)] = True

print(sum(num))
