def f(i, j, V):
    global mx
    if sum(mv) == 4:
        if si == i and sj == j:
            mx = max(mx, len(V))
        return

    for d in range(4):
        if not mv[d]:
            if d != 0 and not mv[d-1]:
                return
            ni = i + move[d][0]
            nj = j + move[d][1]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] not in V:
                visited[ni][nj] = 1
                mv[d] = 1
                f(ni, nj, V[:] + [arr[ni][nj]])
                mv[d] = 0
                f(ni, nj, V[:] + [arr[ni][nj]])
                visited[ni][nj] = 0

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = -1


    move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    mv = [0, 0, 0, 0]
    for i in range(N):
        for j in range(N):
            if i not in [0, N-1] or j not in [0, N-1]:
                visited = [[0] * N for _ in range(N)]
                si, sj = i, j
                f(i, j, [])
    print(mx)
