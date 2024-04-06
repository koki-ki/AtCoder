n, a, b = map(int, input().split())
d = list(map(int, input().split()))
d = [di % (a + b) for di in d]

d.sort()
next_d = [di + (a + b) for di in d]
extended_d = d + next_d

n_extended = len(extended_d)
for i in range(n_extended - 1):
    if extended_d[i + 1] - extended_d[i] > b:
        print("Yes")
        exit()

print("No")
