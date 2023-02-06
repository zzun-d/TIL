from collections import defaultdict
import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
INF = 2e11

distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y, t = map(int, input().split())
    graph[x].append((y, t))


q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost 
            heapq.heappush(q, (cost, i[0]))

for i in range(1, N+1):
    ans = 0
    for j in range(1, N+1):
        ans += distance[i] + distance[j]
    print(ans)

