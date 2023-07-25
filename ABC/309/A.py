a, b = map(int, input().split())
a -= 1
b -= 1
distance = abs(a // 3 - b // 3) + abs(a % 3 - b % 3)
if distance == 1 and a // 3 == b // 3:
    print('Yes')
else:
    print('No')
