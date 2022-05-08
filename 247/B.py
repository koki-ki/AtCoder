n = int(input())
s = list()
t = list()
adana = list()

for i in range(n):
    S, T = input().split()
    s.append(S)
    t.append(T)
    adana.append(S)
    if S != T:
        adana.append(T)

adana = [name for name in adana if adana.count(name) == 1]

if len(adana) < n:
    print('No')
    exit()

for i in range(n):
    if s[i] in adana:
        adana.remove(s[i])
    elif t[i] in adana:
        adana.remove(t[i])
    elif s[i] == t[i]:
        continue
    else:
        print('No')
        exit()

print('Yes')


