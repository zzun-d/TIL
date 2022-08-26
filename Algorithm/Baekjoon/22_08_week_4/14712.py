N, M = map(int, input().split())
nemmo = [[0]*M for _ in range(N)]
cnt = 0

def bfs(i, j, arr):
    global cnt

    if i >= N:
        if arr[N-1][M-1] and arr[N-2][M-1] and arr[N-1][M-2] and arr[N-2][M-2]:
            return
        cnt += 1
        return

    if i-1 >= 0 and j-2 >= 0 and i < N and j-1 < M:
        if arr[i][j-1] and arr[i-1][j-1] and arr[i][j-2] and arr[i-1][j-2]:
            return
    if j >= M:
        bfs(i+1, 0, arr)

    else:
        arr[i][j] = 1
        bfs(i, j+1, arr)
        arr[i][j] = 0
        bfs(i, j+1, arr)

if N == 1 or M == 1:
    cnt = 2**(N*M)
else:
    bfs(0, 0, nemmo)
print(cnt)