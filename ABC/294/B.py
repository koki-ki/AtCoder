h, w = map(int, input().split())

alphabets = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = []

for _ in range(h):
    news = ""
    a = list(map(int, input().split()))
    for i in range(w):
        news += str(alphabets[a[i]])
    s.append(news)

for i in range(h):
    print(s[i])