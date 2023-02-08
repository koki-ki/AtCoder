from collections import defaultdict
# リストの行列転置
def transpose(s: list) -> list:
    h = len(s)
    w = len(s[0])
    transposed_s = [['' for _ in range(h)] for _ in range(w) ]
    for i in range(w):
        for j in range(h):
            transposed_s[i][j] = s[j][i]
    return transposed_s

# main
h, w = map(int, input().split())
s = []
t = []
for _ in range(h):
    s.append(list(input()))
for _ in range(h):
    t.append(list(input()))

s = transpose(s)
t = transpose(t)

dict_s = defaultdict(int)
dict_t = defaultdict(int)


for si in s:
    si = ''.join(si)
    dict_s[si] += 1
for ti in t:
    ti = ''.join(ti)
    dict_t[ti] += 1

if dict_s == dict_t:
    print('Yes')
else:
    print('No')