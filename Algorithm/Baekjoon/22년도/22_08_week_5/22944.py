from collections import deque
import sys
input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N, H, D = map(int, input().split())
arr = []
si = sj = -1
for i in range(N):
    arr.append(list(input()))

    if si < 0:
        for j in range(N):
            if arr[i][j] == 'S':
                si, sj = i, j
                break

def bfs():
    visited = [[0]*N for _ in range(N)]
    q = deque([(si, sj, H, 0, 0)])
    visited[si][sj] = H

    while q:
        i, j, h, d, cnt = q.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'E':
                    print(cnt + 1)
                    return
                
                n_h = h
                n_d = d

                if arr[ni][nj] == 'U':
                    n_d = D
                
                if n_d == 0:
                    n_h -= 1
                else:
                    n_d -= 1

                if n_h == 0:
                    continue

                if visited[ni][nj] < n_h:
                    visited[ni][nj] = n_h
                    q.append((ni, nj, n_h, n_d, cnt+1))
    print(-1)

bfs()
                
