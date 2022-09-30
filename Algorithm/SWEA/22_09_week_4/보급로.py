from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    dp = [[20000]*N for _ in range(N)]
    dp[0][0] = arr[0][0]

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and dp[nx][ny] > dp[x][y] + arr[nx][ny]:
                dp[nx][ny] = dp[x][y] + arr[nx][ny]
                queue.append((nx, ny))

    print(f'#{tc} {dp[-1][-1]}')
