a, b, x = map(int, input().split())
cnt = 0
hajimenoamari = a % x
nokori = b - (x - hajimenoamari)
cnt += nokori // x
print(cnt)