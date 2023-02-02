import sys
import heapq

INF = 3e5

def input():
    return sys.stdin.readline().rstrip()

V, E = map(int, input().split())
K = int(input())
djLst = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    djLst[u].append((v, w))

q = []
heapq.heappush(q, (0, K))
distance[K] = 0

while q:
    w, v = heapq.heappop(q)

    if distance[v] < w:
        continue

    for lst in djLst[v]:
        cost = w + lst[1]
        if cost < distance[lst[0]]:
            distance[lst[0]] = cost
            heapq.heappush(q, (cost, lst[0]))

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")

    else:
        print(distance[i])