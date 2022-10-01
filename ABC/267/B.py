s = [0] + list(map(int, list(input())))
if s[1] == 1:
    print('No')
    exit()

retsu = []
retsu.append([s[7]])
retsu.append([s[4]])
retsu.append([s[8], s[2]])
retsu.append([s[5], s[1]])
retsu.append([s[9], s[3]])
retsu.append([s[6]])
retsu.append([s[10]])

for i in range(1, 6):

    if sum(retsu[i]) == 0:
        hidari = 0
        migi = 0
        for j in range(0, i):
            hidari += sum(retsu[j])
        for j in range(i, 7):
            migi += sum(retsu[j])
        if hidari != 0 and migi != 0:
            print('Yes')
            exit()

print('No')
