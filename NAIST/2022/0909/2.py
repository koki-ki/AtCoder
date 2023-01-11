n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (2000001)
shurui = 0
for a_ in a:
    if cnt[a_] == 0:
        shurui += 1
    cnt[a_] += 1

if shurui <= k:
    print(0)
    exit()

cnt.sort()
kakikaeru = shurui - k
i = 1
ans = 0

while kakikaeru > 0:
    if cnt[i] != 0:
        kakikaeru -= 1
        ans += cnt[i]
    i += 1

print(ans)
