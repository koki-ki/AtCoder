a = []
while True:
    n = int(input())
    a.append(n)
    if n == 0:
        break


a.reverse()
for i in range(len(a)):
    print(a[i])
