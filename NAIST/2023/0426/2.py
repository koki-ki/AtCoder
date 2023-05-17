n = int(input())

cnt = 0
for i in range(1, n + 1, 2):
    cnt_i = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt_i += 1
    if cnt_i == 8:
        cnt += 1

print(cnt)