T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            kil = 0
            for k in range(M):
                for l in range(M):
                    kil += arr[i+k][j+l]
            if kil > k_max:
                k_max = kil
    print(f'#{t} {k_max}')