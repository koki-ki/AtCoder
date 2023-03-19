import heapq

n, q = map(int, input().split())
ans = []
uncalled = [i + 1 for i in range(n)]
called = []
went = [False for _ in range(n + 1)]

heapq.heapify(uncalled)
heapq.heapify(called)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        n = heapq.heappop(uncalled)
        heapq.heappush(called, n)
    elif query[0] == 2:
        _, x = query
        went[x] = True
    else:
        while True:
            x = heapq.heappop(called)
            if went[x]:
                continue
            else:
                ans.append(x)
                heapq.heappush(called, x)
                break

for a in ans:
    print(a)
