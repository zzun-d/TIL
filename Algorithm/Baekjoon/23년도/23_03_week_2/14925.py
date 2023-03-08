M, N = map(int, input().split())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(M) ]
mx = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        if arr[i][j] > 0:
            arr[i][j] = 0
        else:
            arr[i][j] = min(arr[i-1][j], arr[i-1][j-1], arr[i][j-1]) + 1
            mx = max(mx, arr[i][j])
print(mx)