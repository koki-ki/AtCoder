n, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
sk = s[:k]
sk.sort()

for name in sk:
    print(name)