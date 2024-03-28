b = int(input())

i = 1
while i ** i <= b:
    if i ** i == b:
        print(i)
        exit()
    i += 1

print(-1)
