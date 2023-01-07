N = int(input())

if N < 4:
    if N == 1:
        print(0)
    else:
        print(1)
else:
    dp = [0]*(N+1)
    dp[2] = dp[3] = 1
    for i in range(4, N+1):
        mn = dp[i-1]
        if not i % 2:
            mn = min(mn, dp[i//2])
        if not i % 3:
            mn = min(mn, dp[i//3])
        dp[i] = mn + 1
    print(dp[N])
    
        
        