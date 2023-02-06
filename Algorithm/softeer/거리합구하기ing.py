import sys
import heapq
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
inf = 2e5*N
distance = [inf]*(N+1)
edgeList = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y, t = map(int, input().split())
    edgeList[x].append((t, y))
    edgeList[y].append((t, x))

parentTree = [0]*(N+1)
q = deque([1])
visited = [False] * (N+1)
while q:
    n = q.popleft()
    visited[n] = True
    for _, node in edgeList[n]:
        if not visited[node]:
            parentTree[node] = n
            q.append(node)


isSubTree = [set() for _ in range(N+1)]
visited = [False] * (N+1)


def set_sub_tree(s):
    visited[s] = True
    for _, e in edgeList[s]:
        if not visited[e]:
            visited[e] = True
            isSubTree[s] |= set_sub_tree(e)

    isSubTree[s].add(s)

    return isSubTree[s]


set_sub_tree(1)

distance[1] = 0
q = []
heapq.heappush(q, (0, 1))
while q:
    t, node = heapq.heappop(q)

    if distance[node] < t:
        continue

    for c, target in edgeList[node]:
        cost = c + distance[node]
        if distance[target] > cost:
            distance[target] = cost
            heapq.heappush(q, (cost, target))
std = sum(distance[1:])


for i in range(2, N+1):
    ans = 0
    now = i
    while True:
        if parentTree[now] == 1:
            break
        now = parentTree[now]
    nodes = isSubTree[now] - isSubTree[i]
    for n in nodes:
