N = int(input())

arr = [list(map(int, input().split())) for _ in range()]
visited = [[[] for _ in range(N)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            d = 1

            while j+d < N and i+d < N:
                if arr[i+d][j+d] == 1:
                    visited[i][j].append((i+d, j+d))
                d += 1

            d = 1
            while j+d < N and i-d >= 0:
                if arr[i-d][j+d] == 1:
                    visited[i][j].append((i-d, j+d))

            d = 1
            while j-d < N and i-d >= 0:
                if arr[i-d][j-d] == 1:
                    visited[i][j].append((i-d, j-d))

            d = 1
            while j-d < N and i+d >= 0:
                if arr[i+d][j-d] == 1:
                    visited[i][j].append((i+d, j-d))
            visited[i][j] = [len(visited[i][j])] + visited[i][j]


