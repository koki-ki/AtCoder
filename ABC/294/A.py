n = int(input())
a = list(map(int, input().split()))
b = []
for a_ in a:
    if a_ % 2 == 0:
        b.append(a_)
print(*b)