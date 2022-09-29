from collections import deque


D = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 하 우 상 좌
pos_lst = [[1, 2, 4, 7], [1, 3, 6, 7], [1, 2, 5, 6], [1, 3, 4, 5]]
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    ans = 0
    queue = deque([(R, C)])
    for _ in range(L-1):
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if arr[r][c] == 0:
                continue
            elif arr[r][c] == 1:
                d_l = [0, 1, 2, 3]
            elif arr[r][c] == 2:
                d_l = [0, 2]
            elif arr[r][c] == 3:
                d_l = [1, 3]
            elif arr[r][c] == 4:
                d_l = [1, 2]
            elif arr[r][c] == 5:
                d_l = [0, 1]
            elif arr[r][c] == 6:
                d_l = [0, 3]
            else:
                d_l = [2, 3]
            for d in d_l:
                nr = r + D[d][0]
                nc = c + D[d][1]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] in pos_lst[d]:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    ans += 1
    if ans:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 1')



