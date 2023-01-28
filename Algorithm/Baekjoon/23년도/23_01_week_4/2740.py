N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
for i in range(N):
    ans = []
    for j in range(K):
        value = 0
        for k in range(M):
            value += A[i][k]*B[k][j]
        ans.append(value)
    print(*ans)
