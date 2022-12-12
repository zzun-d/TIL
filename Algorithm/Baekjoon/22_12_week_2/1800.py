from collections import deque, defaultdict

N, P, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(P):
    n1, n2, price = map(int, input().split())
    graph[n1].append((n2, price))
    graph[n2].append((n1, price))


queue = deque([(1, {1}, [0])])
cost = -1
while queue:
    num, cable_set, prices = queue.popleft()
    for n, p in graph[num]:
        pass