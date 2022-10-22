n = int(input())
a = list(map(int, input().split()))

ameba = [0] * (2 * n + 2)

for i, a_ in enumerate(a, 1):
    ameba[2 * i] = ameba[a_] + 1
    ameba[2 * i + 1] = ameba[a_] + 1

for i in range(1, 2 * n + 2):
    print(ameba[i])
