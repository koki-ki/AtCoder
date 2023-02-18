s = input()
t = input()
a = ["R G B", "G B R", "B R G"]
ans = "Yes" if (s in a) == (t in a) else "No"
print(ans)