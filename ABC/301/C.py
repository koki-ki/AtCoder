from collections import defaultdict

s = list(input())
t = list(input())
length = len(s)

atcoder = list('atcoder')

num_s = defaultdict(int)
num_t = defaultdict(int)
diff = defaultdict(int)

for si in s:
    num_s[si] += 1

for ti in t:
    num_t[ti] += 1

chars = set(s) | set(t)

for c in chars:
    if c == '@':
        continue
    if num_s[c] >= num_t[c]:
        num_s[c] -= num_t[c]
        num_t[c] = 0
    else:
        num_t[c] -= num_s[c]
        num_s[c] = 0

    diff[c] = num_s[c] - num_t[c]


    # 論外
    if diff[c] != 0 and c not in atcoder:
        print('No')
        exit()

num_left_s = sum(num_s.values()) - num_s['@']
num_left_t = sum(num_t.values()) - num_t['@']

num_s['@'] -= num_left_t
num_t['@'] -= num_left_s



if num_s['@'] >= 0 and num_t['@'] >= 0:
    print('Yes')
else:
    print('No')