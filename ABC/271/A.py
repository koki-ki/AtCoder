n = int(input())
n = hex(n)
n = n[2:]
if len(n) == 1:
    n = '0' + n
n = n.upper()
print(n)
