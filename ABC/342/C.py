from string import ascii_lowercase

n = int(input())
s = input()
q = int(input())
queries = [list(input().split()) for _ in range(q)]

mapping_from = ascii_lowercase
mapping_to = ascii_lowercase

for query in queries:
    c, d = query
    mapping_to = mapping_to.replace(c, d)

mapping = dict(zip(mapping_from, mapping_to))

s = s.translate(str.maketrans(mapping_from, mapping_to))
print(s)
