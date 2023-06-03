a, b = map(int, input().split())

if a % b == 0:
    ans = a // b
else:
    ans = a // b + 1

print(ans)