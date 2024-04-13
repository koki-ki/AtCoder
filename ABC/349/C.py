s = input().upper()
t = input()


def check1(s, t):
    n = len(s)
    t_list = list(t)
    j = 0

    for i in range(n):
        if s[i] == t_list[j]:
            j += 1
            if j == len(t):
                return True

    return False


def check2(s, t):
    if t[2] != "X":
        return False

    t = t[0] + t[1]
    return check1(s, t)


if check1(s, t) or check2(s, t):
    print("Yes")
else:
    print("No")
