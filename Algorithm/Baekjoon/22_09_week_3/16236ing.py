from collections import deque


def bfs(s, i, j):
    queue = deque([(i, j)])
    t = 0
    target = []
    while queue:
        t += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and s >= arr[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                    if (ni, nj, arr[ni][nj]) in fish_lst:
                        target.append((ni, nj))

        if target:
            target.sort()
            fish[arr[target[0][0]][target[0][1]]].remove((target[0][0], target[0][1], arr[target[0][0]][target[0][1]]))
            arr[target[0][0]][target[0][1]] = 0
            return target[0][0], target[0][1], t
    return False, False, False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
fish = [[] for _ in range(7)]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if arr[i][j] == 9:
                shark = (2, i, j)
            else:
                fish[arr[i][j]].append((i, j, arr[i][j]))

T = 0
upgrade = 2
while True:
    visited = [[0]*N for _ in range(N)]
    s, i, j = shark

    for f in range(s):
        fish_lst = []
        fish_lst += fish[f]
        
    ni, nj, t = bfs(s, i, j)
    if not t:
        break
    upgrade -= 1
    T += t
    if not upgrade:
        s += 1
        upgrade = s
    shark = (s, ni, nj)

print(T)