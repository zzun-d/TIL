N = int(input())

dp = [-1] * 5001
dp[3] = dp[5] = 1

for i in range(6, N+1):
    if dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
    elif dp[i-3] != -1:
        dp[i] = dp[i-3] + 1

print(dp[N])