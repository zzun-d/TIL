from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            queue.append((i, j))
cnt = 0
tmp = True
while queue:
    nxt = []
    meltes = []
    for i, j in queue:
        melt = 0
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] <= 0:
                melt += 1
        meltes.append(melt)

    for i in range(len(queue)):
        x = queue[i][0]
        y = queue[i][1]
        arr[x][y] -= meltes[i]
        if arr[x][y] > 0:
            nxt.append((x, y))
    queue = nxt[:]
    if not nxt:
        break
    ice = deque([nxt[0]])
    ice_cnt = 1
    visited = [[0]*M for _ in range(N)]
    visited[nxt[0][0]][nxt[0][1]] = 1
    while ice:
        i, j = ice.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] > 0 and not visited[ni][nj]:
                visited[ni][nj] = 1
                ice.append((ni, nj))
                ice_cnt += 1
    cnt += 1
    if ice_cnt != len(queue):
        tmp = False
        break

    


if tmp:
    print(0)
else:
    print(cnt)