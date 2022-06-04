n = int(input())
s = list()
for i in range(n):
    s.append(input())

dict_ = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in range(10):
    # new_s = []
    # new_s_i = []


    check = []
    t = 0

    while len(check) < n:
        print(dict_)

        for j in range(n):
            if s[j][t % 10] == str(i) and j not in check:
                check.append(j)
                t += 1
                continue
            t += 1

    dict_[i] = t
    print(i)

ans = min(dict_.values())
print('ans', ans)
