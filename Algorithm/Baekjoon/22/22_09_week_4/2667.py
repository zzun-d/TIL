from collections import deque


def bfs(x, y):
    global gr

    queue = deque([(x, y)])
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                arr[nx][ny] = gr
                cnt += 1
                queue.append((nx, ny))
    info.append(cnt)


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
info = []
gr = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            gr += 1
            arr[i][j] = gr
            bfs(i, j)

print(gr - 1)
for i in sorted(info):
    print(i)