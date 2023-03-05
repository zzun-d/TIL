N = int(input())
lst = list(map(int, input().split()))
dp = [0]*N
dp[0] = 1
for i in range(1, N):
    for j in range(0, i):
        if lst[i] > lst[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))