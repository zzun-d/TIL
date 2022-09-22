from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
cnt = 1
queue = deque([(0, 0)])
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
tmp = False
while queue:
    for _ in range(len(queue)):
        i, j = queue.popleft()
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == '1':
                visited[ni][nj] = 1
                queue.append((ni, nj))
                if ni == N-1 and nj == M-1:
                    tmp = True
                    queue = False
                    break
        if tmp:
            break
    cnt += 1

print(cnt)