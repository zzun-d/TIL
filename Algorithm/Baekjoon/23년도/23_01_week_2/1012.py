import sys
sys.setrecursionlimit(10**6)


def search(x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if N > nx >= 0 and M > ny >= 0 and arr[nx][ny] == 1:
            arr[nx][ny] = 0
            search(nx, ny)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    arr = [[0]*M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                ans += 1
                search(i, j)
                    
    print(ans)
