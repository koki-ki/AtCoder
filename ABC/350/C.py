n = int(input())
a = [None] + list(map(int, input().split()))

num_indices = {}
for i in range(1, n + 1):
    num_indices[a[i]] = i

operations = []

for i in range(1, n):
    num = a[i]
    if num == i:
        continue
    i_index = num_indices[i]
    a[i], a[i_index] = i, num
    num_indices[a[i]] = i
    num_indices[a[i_index]] = i_index
    ii, jj = min(i, i_index), max(i, i_index)
    operations.append((ii, jj))

print(len(operations))
for ii, jj in operations:
    print(ii, jj)

# print(a)
