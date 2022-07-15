from xml.etree.ElementTree import TreeBuilder


w = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
flg = True
for i in range(26):
    if w.count(alphabet[i]) % 2 != 0:
        print('No')
        exit()
print('Yes')