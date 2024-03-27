from string import ascii_lowercase

s = input()
cnt = {c: s.count(c) for c in s}
most_freq = max(cnt.values())

for c in ascii_lowercase:
    if c not in cnt:
        continue
    if cnt[c] == most_freq:
        print(c)
        break
