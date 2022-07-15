q = int(input())
box = []

cnt = 0

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
        ans = sum(box[cnt: cnt + c])
        print(ans)
        cnt += c

