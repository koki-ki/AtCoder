from collections import deque
s = input()
Q = int(input())
s = deque(s)

is_Rev = False
for _ in range(Q):
    q = list(input().split())
    if q[0] == '1':
        ''' '''
        is_Rev = not(is_Rev)
    else:
        f = int(q[1])
        c = q[2]
        # print('***', f, is_Rev)
        if f == 1 and is_Rev is False:
            s.appendleft(c)
        elif f == 1 and is_Rev is True:
            s.append(c)
        elif f == 2 and is_Rev is True:
            s.appendleft(c)
        elif f == 2 and is_Rev is False:
            s.append(c)

    # print(_ + 1, s)
    # print(s)

if is_Rev:
    print(''.join(list(reversed(s))))
else:
    print(''.join(list(s)))
# s = list(s)
# if is_Rev:
#     s = ''.join(s[::(-1)])
# else:
#     s = ''.join(s)
# print(s)
