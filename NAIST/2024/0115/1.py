n, x = map(int, input().split())
alphabet = [chr(i) * n for i in range(65, 65+26)]
S = ''.join(alphabet)
ans = S[x - 1]
print(ans)
