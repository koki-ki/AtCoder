n = int(input())

alphabets = 'abcdefghijklmnopqrstuvwxyz'
ans = ''

while n:
    n -= 1
    index = n % 26
    n //= 26
    ans += alphabets[index]

ans = ans[::-1]
print(ans)