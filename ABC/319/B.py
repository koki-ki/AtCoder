n = int(input())
s = ["-" for _ in range(n + 1)]

for i in range(n + 1):
    flag = False
    for j in range(1, 10):
        if n % j != 0:
            continue
        if i % (n // j) == 0:
            s[i] = str(j)
            flag = True
            break

ans = "".join(s)
print(ans)
