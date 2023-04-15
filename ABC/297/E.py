import heapq
from copy import deepcopy

n, k = map(int, input().split())
a = list(map(int, input().split()))
heapa = deepcopy(a)
nextheap = []
heapq.heapify(heapa)
heapq.heappush(heapa, 0)
heapq.heapify(nextheap)

numbers = set([0] + a)

while len(numbers) < k:

    if len(heapa) == 0:
        heapa, nextheap = nextheap, heapa
    # print(heapa)

    cheapest = heapq.heappop(heapa)

    # print('cheapest:', cheapest)
    for a_ in a:
        new_number = cheapest + a_
        # print('added:', a_)
        # print('new number:', new_number)
        if new_number not in numbers:
            heapq.heappush(nextheap, new_number)
            numbers.add(new_number)

numbers = list(numbers)
numbers.sort()
# print(numbers)
ans = numbers[k]
print(ans)

