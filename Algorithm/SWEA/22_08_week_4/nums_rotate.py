T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    ans = []
    for _ in range(3):
        for i in range(N):
            for j in range(i+1, N):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

        n_arr = [0] * N

        for i in range(N):
            for j in range(N//2):
                arr[i][j], arr[i][-j-1] = arr[i][-j-1], arr[i][j]
            n_arr[i] = ''.join(arr[i][:])

        ans.append(n_arr)
    print(f'#{t}')
    for i in range(N):
        for j in range(3):
            print(ans[j][i], end=' ')
        print()