n = int(input())
a = list(map(int, input().split()))
cards = [4 for _ in range(n + 1)]
cards[0] = 0

for ai in a:
    cards[ai] -= 1

for i, c in enumerate(cards):
    if c == 1:
        print(i)