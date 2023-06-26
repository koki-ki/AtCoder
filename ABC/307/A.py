n = int(input())
a = [0] + list(map(int, input().split()))

ans = [sum(a[i *7 +1: i * 7 + 8]) for i in range(n)]
print(*ans)