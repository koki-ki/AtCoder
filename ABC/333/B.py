SHORTEST = set(["AB", "BC", "CD", "DE", "AE"])

s = ''.join(sorted(input()))
t = ''.join(sorted(input()))

if (s in SHORTEST and t in SHORTEST) or (s not in SHORTEST and t not in SHORTEST):
    print("Yes")
else:
    print("No")
