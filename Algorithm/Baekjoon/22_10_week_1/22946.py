from collections import defaultdict, deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def find_set(n, k):
    for i in graph[k]:
        x1, y1, r1 = lst[i]
        x2, y2, r2 = lst[n]
        if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 > r1 + r2:
            continue
        elif r1 > r2:
            find_set(n, i)
            break
        else:
            graph[k].remove(i)
            graph[k].append(n)
            graph[n].append(i)
            for j in graph[k]:
                x1, y1, r1 = lst[j]
                if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 > r1 + r2:
                    continue
                else:
                    graph[k].remove(j)
                    graph[n].append(j)
            break
    else:
        graph[k].append(n)
    

N = int(input())
lst = [(0, 0, 1010000)]
graph = defaultdict(list)
graph[0].append(1)
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
for i in range(2, N+1):
    find_set(i, 0)

for i in list(graph.keys()):
    for j in graph[i]:
        if not i in graph[j]:
            graph[j].append(i)

queue = deque()
queue.append((0, 0))
visited = [0] * (N+1)
visited[0] = 1
path = []
while queue:
    n, cnt = queue.popleft()
    for i in graph[n]:
        if not visited[i]:
            visited[i] = 1
            queue.append((i, cnt+1))
cnt 