def solution(x, y, n):
    dp = [1e6] * (y+1)
    dp[x] = 0
    for i in range(x+1, y+1):
        if not i % 2:
            if not i % 3:
                dp[i] = min(dp[i-n], dp[i//2], dp[i//3]) + 1
            else:
                dp[i] = min(dp[i-n], dp[i//2]) + 1
        else:
            if not i % 3:
                dp[i] = min(dp[i-n], dp[i//3]) + 1
            else:
                dp[i] = dp[i-n] + 1
    if dp[y] >= 1e6:
        return -1
    return dp[y]