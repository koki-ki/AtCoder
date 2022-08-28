n, a, b = map(int, input().split())
s = 'x' + input()

tsuuka = 0
kaigai = 1
for i in range(1, n + 1):

    if s[i] == 'a' and tsuuka < a + b:
        tsuuka += 1
        print('Yes')
    elif s[i] == 'b':
        if kaigai <= b and tsuuka < a + b:
            print('Yes')
            tsuuka += 1

        else:
            print('No')
        kaigai += 1
    else:
        print('No')