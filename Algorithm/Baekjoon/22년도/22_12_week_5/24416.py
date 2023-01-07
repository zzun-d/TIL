n = int(input())
dp = [0, 1, 1] + [0] * (n-2)
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n], n-2)
