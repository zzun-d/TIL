def bfs():  # 너비 우선 탐색
    if not queue:  # 종료 조건(queue 빔)
        return
    v = queue.pop(0)  # queue 맨 첫 요소 pop

    for t in adjlst[v]:  # 해당 요소와 연결된 노드 탐색
        if not visited[t]:  # 노드가 방문 전이면 ans, queue append & 방문 갱신
            visited[t] = True
            ans.append(t)
            queue.append(t)
    bfs()  # bfs 재귀


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjlst = [[] for _ in range(V + 1)]  # 노드 연결관계 리스트 초기화
    visited = [0, True] + ([False] * (V - 1))  # 방문 여부
    queue = [1]
    ans = [1]

    for _ in range(E):  # 연결관계 리스트 갱신
        s, e = map(int, input().split())
        adjlst[s].append(e)
        adjlst[e].append(s)

    bfs()  # bfs 실시
    print(f'#{tc}', *ans)  # 방문경로 출력
