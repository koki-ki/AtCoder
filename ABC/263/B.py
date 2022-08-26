n = int(input())
p = [0, 0]
p.extend(list(map(int, input().split())))

for i in range(n + 1):
    # print(i)
    if p[i] == 1:
        one = i

#
# print(one)
cnt = 0
i = one

while True:
    for j in range(n + 1):
        if i == p[j]:
            i = j
            break
    cnt += 1

    if i == n:
        break

print(cnt + 1)


