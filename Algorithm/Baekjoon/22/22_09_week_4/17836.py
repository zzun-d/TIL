from collections import deque


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque([(0, 0, 0, 0)])
visited = [[0]*M for _ in range(N)]
visited2 = [[0]*M for _ in range(N)]

during_time = 0
tmp = True
while queue and tmp:
    x, y, p, t = queue.popleft()
    if t == T:
        continue

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if p == 1:
            if 0 <= nx < N and 0 <= ny < M and not visited2[nx][ny]:
                visited2[nx][ny] = 1
                if nx == N-1 and ny == M-1:
                    during_time = t+1
                    tmp = False
                    break
                else:
                    queue.append((nx, ny, 1, t+1))
        else:
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] != 1:
                    visited[nx][ny] = 1
                    if nx == N-1 and ny == M-1:
                        during_time = t+1
                        tmp = False
                        break

                    elif arr[nx][ny] == 2:
                        queue.append((nx, ny, 1, t+1))
                    else:
                        queue.append((nx, ny, p, t+1))

if tmp:
    print("Fail")
else:
    print(during_time)
