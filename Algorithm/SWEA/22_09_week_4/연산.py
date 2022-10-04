from collections import deque


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    dp = [-1]*1000001
    dp[N] = 0
    lst = deque([N])
    while dp[M] < 0:
        n = lst.popleft()

        if n*2 <= 1000000 and dp[n*2] < 0:
            dp[n*2] = dp[n] + 1
            lst.append(n*2)
        if n+1 <= 1000000 and dp[n+1] < 0:
            dp[n+1] = dp[n] + 1
            lst.append(n+1)
        if n-1 >= 1 and dp[n-1] < 0:
            dp[n-1] = dp[n] + 1
            lst.append(n-1)
        if n-10 >= 1 and dp[n-10] < 0:
            dp[n-10] = dp[n] + 1
            lst.append(n-10)
    print(f'#{tc} {dp[M]}')