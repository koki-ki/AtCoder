n = int(input())
adj_list = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    adj_mat = list(map(int, input().split()))
    for j in range(1, n + 1):
        if adj_mat[j - 1] == 1:
            adj_list[i].append(j)


for a in adj_list[1:]:
    print(*a)
