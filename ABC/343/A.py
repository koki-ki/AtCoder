a, b = map(int, input().split())
candidates = list(range(0, 10))
candidates.remove(a + b)
print(candidates[0])
