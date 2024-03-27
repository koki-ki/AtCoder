from string import ascii_lowercase, ascii_uppercase

s = input()
if len(s) == 1 and s in ascii_uppercase:
    print("Yes")
elif s[0] in ascii_uppercase and set(s[1:]) <= set(ascii_lowercase):
    print("Yes")
else:
    print("No")
