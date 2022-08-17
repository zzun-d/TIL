def spray(arr, x, y, d, p):
    '''
    :param arr: 파리 맵
    :param x: 중심 x 좌표
    :param y: 중심 y 좌표
    :param d: 분사각도(0 = 십자모양, 1 = X모양)
    :param p: 분사파워
    :return: 죽은 파리 수
    '''
    ans = arr[x][y]
    if d:
        for i in range(1, p):
            if x+i < N and y+i < N:
                ans += arr[x+i][y+i]
            if x+i < N and y-i >= 0:
                ans += arr[x+i][y-i]
            if x-i >= 0 and y-i >= 0:
                ans += arr[x-i][y-i]
            if x-i >= 0 and y+i < N:
                ans += arr[x-i][y+i]
    else:
        for i in range(1, p):
            if x-i >= 0:
                ans += arr[x-i][y]
            if x+i < N:
                ans += arr[x+i][y]
            if y-i >= 0:
                ans += arr[x][y-i]
            if y+i < N:
                ans += arr[x][y+i]
    return ans






T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(2):
                kil = spray(arr, i, j, k, M)
                if kil > ans:
                    ans = kil
    print(f'#{t} {ans}')