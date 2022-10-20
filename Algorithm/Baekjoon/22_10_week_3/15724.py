N, M = map(int, input().split())
arr = [[0]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
K = int(input())

for _ in range(K):
    si, sj, ei, ej = map(int, input().split())
    ans = dp[ei][ej] - dp[si][sj-1] - dp[si-1][sj] + dp[si-1][sj-1]
    print(ans)