h, w = map(int, input().split())
ans = (h - 1) * w + (w - 1) * h - (h * w - 1)
print(ans)
