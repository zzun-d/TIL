from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

tmp = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            si, sj = i, j
            visited[si][sj] = 1
            arr[si][sj] = 0
            tmp = True
            break
    if tmp:
        break


queue = deque([(si, sj)])
cnt = 1
while queue:
    for _ in range(len(queue)):
        i, j = queue.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] == 1:
                    arr[ni][nj] = cnt
                    queue.append((ni, nj))
    cnt += 1

for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 1:
            arr[i][j] = -1

for row in arr:
    print(*row)
                