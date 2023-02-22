n = int(input())
s = list(map(int, input().split()))
max_area = max(s)

def area(a, b):
    return 4 * a * b + 3 * a + 3 * b

arieru = set()
for a in range(1, max_area + 1):
    for b in range(1, max_area + 1):
        if area(a, b) > max_area:
            break
        arieru.add(area(a, b))
ans = 0
for s_ in s:
    if s_ not in arieru:
        ans += 1
print(ans)