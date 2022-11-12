n = int(input())

sudeni = set()
flg = True
for _ in range(n):
    s = input()
    if s[0] not in ['H', 'D', 'C', 'S']:
        flg = False
    if s[1] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
        flg = False
    if s in sudeni:
        flg = False
    sudeni.add(s)
if flg:
    print('Yes')
else:
    print('No')
