T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        r_k = c_k = 0
        if arr[i][0]:
            r_k = 1
        if arr[0][i]:
            c_k = 1

        for j in range(1, N):
            if arr[i][j]:
                r_k += 1
            else:
                if r_k == K:
                    ans += 1
                r_k = 0

            if arr[j][i]:
                c_k += 1
            else:
                if c_k == K:
                    ans += 1
                c_k = 0
        if r_k == K:
            ans += 1
        if c_k == K:
            ans += 1
    print(f'#{t} {ans}')
