from collections import deque


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 200000
    queue = deque([(0, 0, 0)])
    visited = [[mx]*N for _ in range(N)]
    visited[0][0] = 0
    while queue:
        for _ in range(len(queue)):
            i, j, f = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > visited[i][j] + 1 + max(0, arr[ni][nj] - arr[i][j]):
                    visited[ni][nj] = visited[i][j] + 1 + max(0, arr[ni][nj] - arr[i][j])
                    queue.append((ni, nj, visited[ni][nj]))
    print(f'#{tc} {visited[N-1][N-1]}')

