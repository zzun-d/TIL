import heapq

lst = []
heapq.heappush(lst, (1, 10))
heapq.heappush(lst, (1, 15))
heapq.heappush(lst, (1, 9))
heapq.heappush(lst, (1, -10))
heapq.heappush(lst, (1, 110))
heapq.heappush(lst, (1, 3))
heapq.heappush(lst, (1, 0))

for _ in range(7):
    print(heapq.heappop(lst))
