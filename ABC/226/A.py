x = float(input())
if x - int(x) >= 0.5:
    x = int(x) + 1
else:
    x = int(x)
print(x)