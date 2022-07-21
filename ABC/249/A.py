a, b, c, d, e, f, x = map(int, input().split())
takahashi = 0
aoki = 0
sec = x
while True:
    takahashi += min(a, max(0,sec)) * b
    sec -= a + c
    if sec <= 0:
        break

sec = x
while True:
    aoki += min(d, max(0, sec)) * e
    sec -= d + f
    if sec <= 0:
        break

if takahashi > aoki:
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')