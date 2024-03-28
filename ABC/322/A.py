n = int(input())
s = " " + input()

for i in range(1, n - 1):
    if s[i:i+3] == "ABC":
        print(i)
        exit()

print(-1)
