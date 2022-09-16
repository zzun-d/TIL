T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[-1]*N for _ in range(N)]
    arr[N//2][N//2] = arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = 1

    for _ in range(M):
        i, j, c = map(int, input().split())
        i -= 1
        j -= 1
        if c == 1:
            arr[i][j] = 1

            for di, dj in [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]:
                ni = i + di
                nj = j + dj
                lst = []
                while True:
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 2:
                            lst.append((ni, nj))
                            ni += di
                            nj += dj
                        elif arr[ni][nj] == 1:
                            for x, y in lst:
                                arr[x][y] = 1
                            break
                        else:
                            break
                    else:
                        break

        else:
            arr[i][j] = 2

            for di, dj in [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]:
                lst = []
                ni = i + di
                nj = j + dj
                while True:
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 1:
                            lst.append((ni, nj))
                            ni += di
                            nj += dj
                        elif arr[ni][nj] == 2:
                            for x, y in lst:
                                arr[x][y] = 2
                            break
                        else:
                            break
                    else:
                        break

    black = 0
    white = 0
    for l in arr:
        black += l.count(1)
        white += l.count(2)
    print(f'#{tc} {black} {white}')