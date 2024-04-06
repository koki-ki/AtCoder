s = input()
n = len(s)
substrings_set = set()
for i in range(n):
    for j in range(i, n):
        substrings_set.add(s[i:j + 1])

ans = len(substrings_set)
print(ans)
