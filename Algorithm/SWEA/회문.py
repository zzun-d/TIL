T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N):
            tmp = True
            for k in range(M//2):
                if arr[j][i+k] != arr[j][i+M-k-1]:
                    tmp = False
                    break
            if tmp:
                print(f'#{t} {"".join(arr[j][i:i+M])}')

    for i in range(N-M+1):
        for j in range(N):
            tmp = True
            for k in range(M//2):
                if arr[i+k][j] != arr[i+M-k-1][j]:
                    tmp = False
                    break
            if tmp:
                ans = ''
                for l in range(i, i+M):
                    ans += arr[l][j]
                print(f'#{t} {ans}')


