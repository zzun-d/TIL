from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, K, 0))

    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = 1
    while queue:
        i, j, k, cnt = queue.popleft()

        if i == (H - 1) and j == (W - 1):
            return cnt

        if k > 0:
            for di, dj in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < H and 0 <= nj < W and not arr[ni][nj] and not visited[ni][nj][k-1]:
                    visited[ni][nj][k-1] = 1
                    queue.append((ni, nj, k-1, cnt + 1))
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < H and 0 <= nj < W and not arr[ni][nj] and not visited[ni][nj][k]:
                visited[ni][nj][k] = 1
                queue.append((ni, nj, k, cnt + 1))
    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
print(bfs())