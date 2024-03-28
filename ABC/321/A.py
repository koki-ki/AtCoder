n_str = input()
n = int(n_str)

if len(n_str) == 1:
    print("Yes")
    exit()

length = len(n_str)
for i in range(length - 1):
    if int(n_str[i]) <= int(n_str[i + 1]):
        print("No")
        exit()

print("Yes")
