n, k = map(int, input().split())
s = input()

t = ""
cnt = 0
for i in range(n):
    if s[i] == "o":
        t += "o"
        cnt += 1
    else:
        t += "x"
    if cnt == k:
        t += "x" * (n - i - 1)
        break
print(t)