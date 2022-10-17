from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def bfs(q, fly):
    dp = [[None]*M for _ in range(N)]
    
    if fly == 'up':
        D = up_d
        dp[-1][0] = arr[-1][0]
    else:
        D = down_d
        dp[-1][-1] = arr[-1][-1]

    while q:
        x, y = q.popleft()
        for dx, dy in D:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if dp[nx][ny] == None:
                    q.append((nx, ny))
                    dp[nx][ny] = dp[x][y] + arr[nx][ny]
                elif dp[x][y] + arr[nx][ny] > dp[nx][ny]:
                    q.append((nx, ny))
                    dp[nx][ny] = arr[nx][ny] + dp[x][y]
    return dp



up_d = [(0, 1), (-1, 0)]
down_d = [(0, -1), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue1 = deque([(N-1, 0)])
queue2 = deque([(N-1, M-1)])

dp1 = bfs(queue1, 'up')
dp2 = bfs(queue2, 'down')
mx = -10010000


for i in range(N):
    for j in range(M):
        if dp1[i][j] + dp2[i][j] > mx:
            mx = dp1[i][j] + dp2[i][j]
print(mx)