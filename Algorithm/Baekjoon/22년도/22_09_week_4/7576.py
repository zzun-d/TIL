from collections import deque
M, N = map(int, input().split())
tomato_box = {}
r_t = deque()
for i in range(N):
    line_tomato = list(map(int, input().split()))
    for j in range(M):
        tomato_box[(i, j)] = line_tomato[j]
        if line_tomato[j] == 1:
            r_t.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day = -1
def spread(r_t):
    global day
    for i in range(len(r_t)):
        x, y = r_t.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < N and 0 <= ny < M and tomato_box[(nx, ny)] == 0:
                tomato_box[(nx, ny)] = 1
                r_t.append((nx, ny))
    day += 1
    return r_t

while len(r_t):
    spread(r_t)


if 0 in tomato_box.values():
    print(-1)
else:
    print(day)