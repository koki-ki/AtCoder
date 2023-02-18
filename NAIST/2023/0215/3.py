n = int(input())
keta = n // 9
if n % 9 == 0:
    keta -= 1
ans = str(n - 9 * keta) * (keta + 1)
print(ans)