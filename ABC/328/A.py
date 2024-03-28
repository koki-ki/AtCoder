n, x = map(int, input().split())
s = map(int, input().split())

ans_list = list(filter(lambda i: i <= x, s))
ans = sum(ans_list)
print(ans)
