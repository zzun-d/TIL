from collections import deque


def bfs(cnt, v, x, y):              # BFS 탐색
    global ans
    if cnt == K:                    # 종료조건 거리가 K
        if x == 0 and y == C-1:         # 종료 지점이 집이면 ans + 1
            ans += 1
        return

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C and not v[nx][ny] and arr[nx][ny] == '.':
            v[nx][ny] = 1
            bfs(cnt + 1, v, nx, ny)
            v[nx][ny] = 0 




R, C, K = map(int, input().split())
arr = [input() for _ in range(R)]
ans = 0
visited = [[0]*C for _ in range(R)]
visited[R-1][0] = 1

bfs(1, visited, R-1, 0)

print(ans)