import heapq

n = int(input())
q = int(input())

boxes = [[] for _ in range(n + 1)]
num_boxes = [set() for _ in range(2 * 10 ** 5 + 1)]


for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, i, j = query
        heapq.heappush(boxes[j], i)
        num_boxes[i].add(j)

    elif query[0] == 2:
        _, i = query
        box = boxes[i]
        box.sort()
        print(*box)

    else:
        _, i = query
        box = list(num_boxes[i])
        box.sort()
        print(*box)