n = int(input())
nbin = bin(n)[2:][::-1]
keta = []
for i in range(len(nbin)):
    if nbin[i] == '1':
        keta.append(i)

for i in range(2 ** len(keta)):
    x = 0
    for j in range(len(keta)):
        if i & 1 << j:
            x += 2 ** j

    print(x)
