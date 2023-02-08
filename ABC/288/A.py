n = int(input())
ans = []
for _ in range(n):
    a, b = map(int, input().split())
    ans.append(a + b)
for a in ans:
    print(a)