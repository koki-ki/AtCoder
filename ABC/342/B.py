n = int(input())
p = list(map(int, input().split()))
q = int(input())
ans = []

for _ in range(q):
    a, b = map(int, input().split())
    a_index = p.index(a)
    b_index = p.index(b)
    if a_index < b_index:
        ans.append(a)
    else:
        ans.append(b)

for i in ans:
    print(i)
