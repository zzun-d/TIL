N = int(input())
lst = list(map(int, input().split()))
dp = [0] * N
dp[0] = lst[0]
for i in range(1, N):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += lst[i]
print(max(dp))