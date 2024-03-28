n = int(input())
s = input()

for i in range(n - 1):
    if s[i:i+2] in ("ab", "ba"):
        print("Yes")
        exit()

print("No")
