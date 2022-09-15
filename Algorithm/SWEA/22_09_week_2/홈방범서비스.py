T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                houses.append((i, j))
    K = N+1
    result = 0
    while True:

        if len(houses)*M < 2*K*(K-1)+1:
            K -= 1
            continue
        for i in range(N):
            for j in range(N):
                cnt = 0
                for h_i, h_j in houses:
                    if abs(i - h_i) + abs(j - h_j) <= K-1:
                        cnt += 1
                
                if cnt*M < 2*K*(K-1)+1:
                    continue
                result = max(cnt, result)
        if result:
            break
        else:
            K -= 1
    print(f'#{tc} {result}')


