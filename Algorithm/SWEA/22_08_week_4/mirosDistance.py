T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    for i in range(N):
        tmp = 0
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
                tmp = 1
                break
        if tmp:
            break

    queue = [(si, sj)]
    visited = [[0]*N for _ in range(N)]
    ans = 1
    while queue:
        i, j = queue.pop(0)

        for di, dj in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != '1':
                visited[ni][nj] = visited[i][j] + 1
                queue.append((ni, nj))
                if arr[ni][nj] == '3':
                    queue = False
                    ans = visited[ni][nj]
                    break

    print(f'#{t} {ans-1}')





