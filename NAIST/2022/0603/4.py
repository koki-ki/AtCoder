q = int(input())
box = []

for i in range(q):
    query = input().split()
    if len(query) == 3:
        x = int(query[1])
        c = int(query[2])
        append_ = [x] * c
        box.extend(append_)
    else:
        ans = 0
        c = int(query[1])
        for j in range(c):
            a = box.pop(0)
            ans += a
        print(ans)

