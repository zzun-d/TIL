T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]          # 노드 리스트

    for _ in range(E):                          # 노드 리스트 갱신
        s, e = map(int, input().split())
        adjList[s].append(e)
        adjList[e].append(s)
    S, G = map(int, input().split())            # 출발 노드, 도착 노드

    queue = [S]                                 # BFS를 위한 queue
    visited = [0] * (V+1)                       # node 거리 저장을 위한 리스트
    ans = 0                                     # ans default 0

    while queue:                                # 방문 노드의 거리를 visited에 갱신 하면서 BFS
        v = queue.pop(0)
        for n in adjList[v]:
            if visited[n] == 0 and n != S:
                visited[n] = visited[v] + 1
                queue.append(n)

            if n == G:                          # 방문한 노드와 도착 노드가 동일하면 ans는 해당 노드 거리, break
                queue = False
                ans = visited[n]
                break

    print(f'#{tc} {ans}')