from collections import Counter
n = int(input())
v = list(map(int, input().split()))
even_numbered = []
odd_numbered = []
for i, v_ in enumerate(v):
    if i % 2 == 0:
        even_numbered.append(v_)
    else:
        odd_numbered.append(v_)
even_counter = Counter(even_numbered)
odd_counter = Counter(odd_numbered)

even_counter_sorted = even_counter.most_common()
odd_counter_sorted = odd_counter.most_common()
ans = 10 ** 10

if even_counter_sorted[0][1] == odd_counter_sorted[0][1]:
    ans1 = sum(even_counter.values()) - even_counter_sorted[0][1]
    ans2 = sum(odd_counter.values()) - odd_counter_sorted[0][1]
