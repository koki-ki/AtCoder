import itertools

q = int(input())
box = []
q_ = []
cnt = 0

for i in range(q):
    query = input().split()
    if len(query) == 3:
        print('1')
        x = int(query[1])
        c = int(query[2])
        append_ = [x] * c
        box.extend(append_)
    else:
        print('2')
        q_.append(int(query[1]))


