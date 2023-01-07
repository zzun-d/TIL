from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

# 좌우상하앞뒤 탐색용 delta
di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())
tsr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]             # 방문 여부 텐서
queue = deque([])                                                   # BFS 탐색용 큐

# 상자 확인하며, 익은 토마토 위치 i, j, k 와 날짜 0을 queue에 append
for i in range(H):                              
    for j in range(N):
        for k in range(M):
            if tsr[i][j][k] == 1:
                queue.append((i, j, k, 0))

# queue가 존재하면 계속 BFS
while queue:
    i, j, k, day = queue.popleft()

    # 상하좌우앞뒤 확인하여 상자 인덱스 내부, 안익은 토마토가 있으면 visited, 텐서, day 갱신
    for d in range(6):
        ni = i + di[d]
        nj = j + dj[d]
        nk = k + dk[d]
        if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and tsr[ni][nj][nk] == 0 and not visited[ni][nj][nk]:
            visited[ni][nj][nk] = 1
            tsr[ni][nj][nk] = 1
            queue.append((ni, nj, nk, day+1))

# BFS 종료 후 익지 않은 토마토 유무 확인 함수, 안익은 토마토 존재시 False 리턴
def tmp(h, n, m):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tsr[i][j][k] == 0:
                    return False
    return True

# 안익은 토마토가 없으면 day 출력, 있으면 -1출력
if tmp(H, N, M):
    print(day)
else:
    print(-1)