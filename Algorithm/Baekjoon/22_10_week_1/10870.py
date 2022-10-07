N = int(input())

dp = [0]*91

for i in range(N+1):
    if i > 1:
        dp[i] = dp[i-1] + dp[i-2]
    else:
        dp[i] = i

print(dp[N])
