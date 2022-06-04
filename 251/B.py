import itertools
n, w = map(int, input().split())
a = list(map(int, input().split()))

num = set()
check_list = []
check_list.append(list(itertools.combinations(a, 1)))
check_list.append(list(itertools.combinations(a, 2)))
check_list.append(list(itertools.combinations(a, 3)))



for i in range(3):
    for j in range(len(check_list[i])):
        if sum(check_list[i][j]) <= w:
            num.add(sum(check_list[i][j]))

print(len(num))
