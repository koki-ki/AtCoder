cards = list(input().split())
cnt = {}

for card in cards:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

if set(cnt.values()) == {2, 3}:
    print('Yes')
else:
    print('No')