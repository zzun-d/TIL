di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]                 # 방문 여부 배열

    for i in range(N):                                      # 시작점 찾기
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break

    ans = 0                     # ans default 0
    stack = [(si, sj)]          # 방문해야 할 지점 stack
    visited[si][sj] = True      # visited 갱신

    while stack:                # 방문해야 할 지점이 있는 동안 루프
        i, j = stack[-1]
        for k in range(4):      # 상하좌우 확인
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:                     # 범위 이내, 길 있고, 방문하지 않았던 지점이면,
                if arr[ni][nj] == 0 and not visited[ni][nj]:    # stack에 append, visited 갱신, break
                    stack.append((ni, nj))
                    visited[ni][nj] = True
                    break

                elif arr[ni][nj] == 3:              # 만약 종료지점이면 ans -> 1, stack -> False, break
                    ans = 1
                    stack = False
                    break
        else:
            stack.pop()         # 상하좌우 모두 갈 곳 없으면 이전 지점으로 돌아감

    print(f'#{t} {ans}')