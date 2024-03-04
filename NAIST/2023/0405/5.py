s = input()
k = int(input())
lens = len(s)
candidates = set()
for i in range(lens - k + 1):
    candidate = s[i: i + k]
    candidates.add(candidate)
print(len(candidates))
