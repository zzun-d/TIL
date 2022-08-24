# def dfs():
#     global visited, ans

#     if len(queue) == 0:
#         return
    
#     i, j = queue.pop(0)
#     for d in dij:
#         ni = i + d[0]
#         nj = j + d[1]
#         if 0 <= ni < N and 0 <= nj < N:
#             if visited[ni][nj] == False:
#                 if arr[ni][nj] == 0:
#                     visited[ni][nj] = True
#                     queue.append((ni, nj))
#                 elif arr[ni][nj] == 3:
#                     ans = 1
#                     return
#     dfs()

dij = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, list(input()))) for _ in range(N)]

    si = sj = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j
                break
        if si >= 0:
            break
    
    queue = [(si, sj)]
    visited = [[0]*N for _ in range(N)]
    visited[si][sj] = 1
    ans = 0

    while queue:
        i, j = queue.pop(0)
        for di, dj in dij:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                elif arr[ni][nj] == 3:
                    ans = 1
                    queue = False
                    break

    print(f'#{tc} {ans}')