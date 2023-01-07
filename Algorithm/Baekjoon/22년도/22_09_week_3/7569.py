from collections import deque


di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())
tsr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
queue = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tsr[i][j][k] == 1:
                queue.append((i, j, k, 0))

while queue:
    i, j, k, c = queue.popleft()
    for d in range(6):
        ni = i + di[d]
        nj = j + dj[d]
        nk = k + dk[d]
        if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and tsr[ni][nj][nk] == 0 and not visited[ni][nj][nk]:
            visited[ni][nj][nk] = 1
            tsr[ni][nj][nk] = 1
            queue.append((ni, nj, nk, c+1))

def tmp(h, n, m):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tsr[i][j][k] == 0:
                    return False
    return True
if tmp(H, N, M):
    print(c)
else:
    print(-1)