def ope1(q):
    return len(q) > 1


def ope2(q):
    return q[-1] == q[-2]


def ope3(q):
    if q[-1] == q[-2]:
        ball, _ = q.pop(), q.pop()
        q.append(ball + 1)


def ope(q):
    flag = True
    while flag:
        flag = ope1(q)
        if flag is False:
            break
        flag = ope2(q)
        if flag is False:
            break
        ope3(q)


# ================================ #
n = int(input())
a = [None] + list(map(int, input().split()))

q = []
for i in range(1, n + 1):
    q.append(a[i])
    ope(q)
    # print(*q)


print(len(q))
