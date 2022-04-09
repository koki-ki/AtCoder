a, b, c, d = map(int, input().split())
takahashi = 60 * 60 * a + 60 * b
aoki = 60 * 60 * c + 60 * d + 1
if takahashi < aoki:
    print('Takahashi')
else:
    print('Aoki')