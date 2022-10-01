n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
ans = 0
for i in range(len(a)):
    if ans != a[i]:
        break
    ans += 1
print(ans)
