T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mps = [list(map(int, input().split())) for _ in range(N)]
    lngst = 0
    for row in mps:
        cnt = 0
        for r in row:
            if r:
                cnt += 1
                if lngst < cnt:
                    lngst = cnt
            else:
                cnt = 0
    for i in range(M):
        cnt = 0
        for j in range(N):
            if mps[j][i]:
                cnt += 1
                if lngst < cnt:
                    lngst = cnt
            else:
                cnt = 0
    print(f'#{t} {lngst}')

