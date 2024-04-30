n = int(input())
a = [-1] + list(map(int, input().split()))

b = [-1] * (n + 1)  # iの次がb[i]

for i in range(1, n + 1):
    if a[i] != -1:
        b[a[i]] = i
    else:
        top = i

cur = top
people = [cur]

while cur != -1:
    people.append(cur)
    cur = b[cur]

print(*people[1:])
