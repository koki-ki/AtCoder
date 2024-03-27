n, l = map(int, input().split())
a = list(map(int, input().split()))
passed_a = list(filter(lambda x: x >= l, a))
print(len(passed_a))
