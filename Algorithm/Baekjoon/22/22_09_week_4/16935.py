from collections import deque


def bfs(i, j, c):

    queue = deque([(i, j)])
    visited[i][j] = 1
    arr[i][j] = c
    sm = 1
    while queue:
        i, j = queue.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj]:
                visited[ni][nj] = 1
                arr[ni][nj] = c
                sm += 1
                queue.append((ni, nj))
    cnt_dict[c] = sm

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt_dict = {}
cnt = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited[i][j]:
            bfs(i, j, cnt)
            cnt += 1
mx = 0
for i in range(N):
    for j in range(M):
        sm = 1
        sm_lst = []
        if not arr[i][j]:
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] and not arr[ni][nj] in sm_lst:
                    sm += cnt_dict[arr[ni][nj]]
                    sm_lst.append(arr[ni][nj])
        mx = max(mx, sm)
print(mx)