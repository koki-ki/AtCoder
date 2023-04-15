a, b = map(int, input().split())

count = 0

while a != b:
    a, b = max(a, b), min(a, b)
    if b == 0:
        count -= 1
        break
    count += a // b
    a %= b

print(count)