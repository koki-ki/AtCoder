import heapq
from copy import deepcopy

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
heapa = deepcopy(a)

heapq.heapify(heapa)
heapq.heappush(heapa, 0)


numbers = set([0] + a)
c = 1

while len(numbers) < k * 10:
    cheapest = heapq.heappop(heapa)

    # print('cheapest:', cheapest)
    for a_ in a:
        new_number = cheapest + a_
        # print('added:', a_)
        # print('new number:', new_number)
        if new_number not in numbers:
            heapq.heappush(heapa, new_number)
            numbers.add(new_number)

numbers = list(numbers)
numbers.sort()
ans = numbers[k]
print(ans)

