n = int(input())
if n >= 42:
    n += 1

ans = "AGC" + "0" * (3 - len(str(n))) + str(n)
print(ans)