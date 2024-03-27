n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

if sum(x) > sum(y):
    print("Takahashi")
elif sum(x) == sum(y):
    print("Draw")
else:
    print("Aoki")
