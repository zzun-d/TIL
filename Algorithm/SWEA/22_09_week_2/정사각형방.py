T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[False]*N for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    mn = 1000000
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                c = 1
                ni = i
                nj = j
                while True:
                    for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nxi = ni + di
                        nxj = nj + dj
                        if 0 <= nxi < N and 0 <= nxj < N and arr[nxi][nxj]-arr[ni][nj] == 1:
                            c += 1
                            ni = nxi
                            nj = nxj
                            visited[nxi][nxj] = True
                            break
                    else:
                        break
                if c > cnt:
                    cnt = c
                    mn = arr[i][j]
                elif c == cnt:
                    mn = min(mn, arr[i][j])
    print(f'#{tc} {mn} {cnt}')