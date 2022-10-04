
def dfs(n, sm):
    global mn
    if mn and sm >= mn:
        return

    if n == N-1:
        if mn:
            mn = min(mn, sm)
        else:
            mn = sm
    else:
        for i in range(N):
            if adjlst[n][i] and not visited[i]:
                visited[i] = 1
                dfs(i, sm + adjlst[n][i])
                visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjlst = [[0]*N for _ in range(N)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        adjlst[a][b] = w
    mn = 0
    visited = [0]*N
    visited[0] = 1
    dfs(0, 0)
    print(f'#{tc} {mn}')



'''
Kruskal

from heapq import heappush, heappop


def  find_set(i):
    while i != rep[i]:
        i = rep[i]
    return i


def union(i, j):
    rep[find_set(j)] = find_set(i)

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = []
    rep = [i for i in range(N+1)]
    cnt = 0
    for _ in range(E):
        a, b, w = map(int, input().split())
        heappush(graph, (w, a, b))
    ans = 0
    while cnt < N-1:
        
        u, v, w = heappop(graph)
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            ans += w
    print(ans)
        
'''