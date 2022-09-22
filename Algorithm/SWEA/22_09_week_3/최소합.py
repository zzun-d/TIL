from heapq import heappop, heappush

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp_arr = [[0]*N for _ in range(N)]
    dp_arr[0][0] = arr[0][0]
    lst = []
    heappush(lst, (arr[0][0], 0,0))

    while not dp_arr[-1][-1]:
        v, i, j = heappop(lst)
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not dp_arr[ni][nj]:
                dp_arr[ni][nj] += dp_arr[i][j] + arr[ni][nj]
                heappush(lst, (dp_arr[ni][nj], ni, nj))
    print(f'#{tc} {dp_arr[-1][-1]}')

