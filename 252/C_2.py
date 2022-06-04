from ast import Dict
from traceback import print_last


n = int(input())
s = list()
for i in range(n):
    s.append(input())

dict_ = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

for i in range(10):
    for j in range(n):
        for k in range(10):
            if s[j][k] == str(i):
                dict_[i].append(k)

print(dict_)

ans_list = []

for i in range(10):
    ans_list.append(max(dict_[i]))
    ichi = []
    for j in range(n):
        if dict_[i][j] in ichi:
            ans_list[i] += 10
        else:
            ichi.append(dict_[i][j])
# print(ans_list)
# # ans = min(ans_list)
# # print(dict_)
# # print(ans_list)
# # print(ans)
# ans = ans_list
# for i in range(10):
#     check = []
#     for j in range(n):
#         if ans_list[i] in check:
#             check.append(ans_list[i][j])

# print(ans_list)
# print(ans)
# print(min(ans))
for i in range(10):
    tmp = dict_[i]
    check = []
    for j in range(n):
        if tmp[j] in check:
            for k in range(j, n):
                dict_[i][k] += 10
        else:
            check.append(tmp[j])
print(dict_)
