def f(i, j, v):
    global mx

    if sum(mv) == 4 and si ==i and sj == j:
        mx = max(mx, sum(v))
        return

    elif arr[i][j] in v:
        return

    v.append(arr[i][j])

    for d in range(4):
        if mv[d]:
            continue
        ni = i + move[d][0]
        nj = j + move[d][1]
        mv[d] = 1
        while 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            visited[ni][nj] = 1
            f(ni, nj, v[:])
            visited[ni][nj] = 0
            ni += move[d][0]
            nj += move[d][1]

T = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = -1

visited = [[0]*N for _ in range(N)]
move = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
mv = [0]*4

for i in range(N):
    for j in range(N):
        if i not in [0, N-1] or j not in [0, N-1]:
            si, sj = i, j
            f(i, j, [arr[i][j]])
print(mx)