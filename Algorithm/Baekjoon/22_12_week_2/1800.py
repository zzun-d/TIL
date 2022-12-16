import heapq, sys

def input():
    return sys.stdin.readline().rstrip()

N, P, K = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(P):
    a, b, c = map(int ,input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c


def total_cost(lst):
    if len(lst) <= K:
        

def bfs(n, v, cables):
    for i in range(N):
        if graph[n][i] == 0 or not v[i]:
            continue
        if i == N-1:
            heapq.heappush(cables, graph[n][i])
            return total_cost(cables)
        v[i] = True
