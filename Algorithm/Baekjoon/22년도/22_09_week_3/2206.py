from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(N)]
visited1 = [[0]*M for _ in range(N)]
visited2 = [[0]*M for _ in range(N)]
visited1[0][0] = visited1[0][0] = 1

queue = deque([(0, 0, 1)])
cnt = 1
while queue:
    cnt += 1
    for _ in range(len(queue)):
        i, j, v = queue.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and v:
                    visited2[ni][nj] = 1
                    queue.append((ni, nj, 0))
                elif arr[ni][nj] == 0:
                    if v and not visited1[ni][nj]:
                        visited1[ni][nj] = 1
                        queue.append((ni, nj, 1))
                    elif not v and not visited2[ni][nj]:
                        visited2[ni][nj] = 1
                        queue.append((ni, nj, 0))
    if (N-1, M-1, 0) in queue or (N-1, M-1, 1) in queue:
        break
if queue:
    print(cnt)
else:
    if N == M == 1:
        print(1)
    else:
        print(-1)


