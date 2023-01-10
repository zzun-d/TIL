import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    dp[i][0] += dp[i-1][0]
    dp[i][-1] += dp[i-1][-1]
    for j in range(1, i):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))