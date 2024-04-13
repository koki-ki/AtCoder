from collections import defaultdict

s = input()

count = {}
for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

count_char = defaultdict(list)

for key in count:
    count_char[count[key]].append(key)

for key in count_char:
    if len(count_char[key]) not in (0, 2):
        print("No")
        exit()

print("Yes")
