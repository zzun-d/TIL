from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def bfs(q, fly):        # q: bfs에 사용되는 queue, fly: 비행의 종류(상승, 하강)
    dp = [[None]*M for _ in range(N)]   # 각 비행 시 좌표 별 얻을 수 있는 점수 배열
    
    if fly == 'up':
        D = [(0, 1), (-1, 0)]
        dp[-1][0] = arr[-1][0]

    else:
        D = [(0, -1), (-1, 0)]
        dp[-1][-1] = arr[-1][-1]

    while q:
        x, y = q.popleft()

        for dx, dy in D:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if dp[nx][ny] == None:                      # 방문하지 않은 지점이면 dp 할당
                    q.append((nx, ny))
                    dp[nx][ny] = dp[x][y] + arr[nx][ny]

                elif dp[x][y] + arr[nx][ny] > dp[nx][ny]:   # 방문은 했으나, 점수가 더 크면 갱신
                    q.append((nx, ny))
                    dp[nx][ny] = arr[nx][ny] + dp[x][y]

    return dp


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


queue1 = deque([(N-1, 0)])      # 출발지점 좌표(상승비행 시작)
queue2 = deque([(N-1, M-1)])    # 도착지점 좌표(하강비행 도착 => 좌측으로 상승비행 시작 좌표로도 볼 수 있음)

dp1 = bfs(queue1, 'up')
dp2 = bfs(queue2, 'down')
mx = -10010000


for i in range(N):
    for j in range(M):
        if dp1[i][j] + dp2[i][j] > mx:
            mx = dp1[i][j] + dp2[i][j]
print(mx)