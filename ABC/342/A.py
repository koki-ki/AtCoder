s = input()
n = len(s)
majority = s[0] if s[0] == s[1] else s[2]

for i in range(n):
    if s[i] != majority:
        print(i + 1)
        exit()
