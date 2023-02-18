n = int(input())
l = [0 for _ in range(2 * 10 ** 5 + 1)]
r = [0 for _ in range(2 * 10 ** 5 + 1)]

for _ in range(n):
    li, ri = map(int, input().split())
    l[li] += 1
    r[ri] += 1

num_of_users = [0 for _ in range(2 * 10 ** 5 + 1)]
for i in range(1, 2 * 10 ** 5 + 1):
    num_of_users[i] = num_of_users[i - 1] + l[i] - r[i]

new_l = []
new_r = []

for i in range(1, 2 * 10 ** 5 + 1):
    if num_of_users[i - 1] == 0 and num_of_users[i] != 0:
        new_l.append(i)
    elif num_of_users[i - 1] != 0 and num_of_users[i] == 0:
        new_r.append(i)

for li, ri in zip(new_l, new_r):
    print(li, ri)
