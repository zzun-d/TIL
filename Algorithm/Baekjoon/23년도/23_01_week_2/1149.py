import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dp = list(map(int, input().split()))
for _ in range(N-1):
    rgb = list(map(int, input().split()))
    dp[0], dp[1], dp[2] = rgb[0] + min(dp[1], dp[2]), rgb[1] + min(dp[0], dp[2]), rgb[2] + min(dp[0], dp[1])
print(min(dp))


