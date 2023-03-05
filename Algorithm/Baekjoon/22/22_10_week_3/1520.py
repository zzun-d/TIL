from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
queue = deque([(0, 0)])
while queue:
    i, j = queue.popleft()
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] < arr[i][j]:
            dp[ni][nj] += 1
            queue.append((ni, nj))
print(dp[-1][-1])