a, b, d = map(int, input().split())
array = [a]
while array[-1] != b:
    array.append(array[-1] + d)

print(*array)
