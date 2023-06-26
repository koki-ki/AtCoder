def is_kaibun(s):
    return s == s[::-1]

n = int(input())
s = [""] + [input() for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        if is_kaibun(s[i] + s[j]):
            print('Yes')
            exit()

print('No')

