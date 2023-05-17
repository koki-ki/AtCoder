n = int(input())
s = input()

dangos = s.split('-')
len_dangos = [len(dango) for dango in dangos]
ans = max(len_dangos)

ans = -1 if ans == 0 else ans
ans = -1 if '-' not in list(s) else ans

print(ans)