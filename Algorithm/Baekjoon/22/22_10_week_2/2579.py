N = int(input())
lst = [0] + [int(input()) for _ in range(N)]
dp = [0] * 301

if N == 1:
    print(lst[1])
elif N == 2:
    print(lst[1] + lst[2])
else:
    dp[1] = lst[1]
    dp[2] = lst[1] + lst[2]
    dp[3] = max(lst[1] + lst[3], lst[2] + lst[3])
    for i in range(4, N+1):
        dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2] + lst[i])
    print(dp[N])