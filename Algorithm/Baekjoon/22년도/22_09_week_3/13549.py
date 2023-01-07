from collections import deque

N, K = map(int, input().split())
dp = [-1]*100001
dp[N] = 0
lst = [N]
if N == 0:
    dp[1] = 1
    lst = [1]

if N >= K:
    print(N-K)

else:
    while dp[K] < 0:
        twice = set(lst)
        nxt = set()
        for l in lst:
            n = dp[l]
            while l < K and l <= 50000 and l > 0:
                l *= 2
                if dp[l] < 0:
                    dp[l] = n
                    twice.add(l)
        lst = list(twice)
        for l in lst:
            if l > K and dp[l-1] < 0:
                dp[l-1] = dp[l] + 1
                nxt.add(l-1)

            elif l < K:
                if dp[l+1] < 0:
                    dp[l+1] = dp[l] + 1
                    nxt.add(l+1)
                if dp[l-1] < 0:
                    dp[l-1] = dp[l] + 1
                    nxt.add(l-1)
        lst = list(nxt)
    
    print(dp[K])