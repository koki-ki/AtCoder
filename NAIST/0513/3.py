n, x = map(int, input().split())
a = list(map(int, input().split()))
known = {x}

while True:
    x = a[x - 1]

    if x in known:
        break
    else:
        known.add(x)

print(len(known))
