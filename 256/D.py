n = int(input())
l = []
r = []
for i in range(n):
    l_, r_ = map(int, input().split())
    l.append(l_)
    r.append(r_)

kukan = [[l[0], r[0]]]
for i in range(1, n):
    for j in range(len(kukan)):
        flg = True
        if l[i] in range(kukan[j][0], kukan[j][1] + 1) and kukan[j][1] < r[i]:
            kukan[j][1] = r[i]
            flg = False

        if l[i] < kukan[j][0] and r[i] in range(kukan[j][0], kukan[j][1] + 1):
            kukan[j][0] = l[i]
            flg = False

        if flg:
            kukan.append([l[i], r[i]])

ans = [[kukan[j][0], kukan[j][1]]]

for i in range(1, len(kukan)):
    for j in range(len(ans)):
        print(ans[j][0])
        print(kukan[i][0])
        if ans[j][0] in range(kukan[i][0], kukan[i][1] + 1) and ans[j][1] in range(kukan[i][0], kukan[i][1] + 1):
            break
        else:
            ans.append([kukan[i][0], kukan[i][1]])

for i in range(len(ans)):
    print(ans[i][0], ans[i][1])