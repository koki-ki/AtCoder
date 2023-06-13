def f(t):
    rt = ''
    l = len(t)
    for i in range(l):
        rt += 'p' if t[l - 1 - i] == 'd' else 'd'
    return rt

n = int(input())
s = input()

print(f(s))
