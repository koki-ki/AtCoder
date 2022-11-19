h, m = map(int, input().split())
while True:
    a = (h // 10) % 10
    b = h % 10
    c = (m // 10) % 10
    d = m % 10

    if 0 <= a * 10 + c <= 23 and 0 <= b * 10 + d <= 59:
        print(h, m)
        exit()

    m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
