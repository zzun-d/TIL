import sys

def input():
    return sys.stdin.readline().rstrip()

T, W = map(int, input().split())

dp = [[0]*(T+1) for _ in range(W+2)]

for i in range(1, T+1):
    t_n = int(input())
    for j in range(1, min(W+2, i+2)):
        if t_n % 2 == j % 2:
            dp[j][i] += max(dp[j][i-1] + 1, dp[j-1][i-1] + 1)
        else:
            dp[j][i] += max(dp[j][i-1], dp[j-1][i-1])
ans = 0
for lst in dp:
    ans = max(lst[-1], ans)
print(ans)
        
