n = int(input())
a = list(set(map(int, input().split())))
a.sort()
ans = a[-2]
print(ans)
