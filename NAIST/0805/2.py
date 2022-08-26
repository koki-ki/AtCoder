A, B, C = map(int, input().split())
nokori = A - B
C -= nokori
print(max(0, C))