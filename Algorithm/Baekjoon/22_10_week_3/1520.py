from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[N*M]*M for _ in range(N)]
dp[0][0] = 0
queue = deque([(0, 0)])
while queue:
    i, j = queue.popleft()
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and dp[ni][nj] > dp[i][j] + 1:
            dp[ni][nj] = dp[i][j] + 1
            queue.append((ni, nj))
print(dp[-1][-1])