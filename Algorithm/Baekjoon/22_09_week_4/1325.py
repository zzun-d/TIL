from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip()

def find(n):
    if dp[n]:
        return dp[n]
    else:
        if graph[n]:
            sm = 1
            for j in graph[n]:
                sm += find(j)
            dp[n] = sm
            return sm
        else:
            dp[i] = 1
            return 1

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

dp = [0]*(N+1)
mx = 0
ans = []
for i in range(1, N+1):
    if dp[i]:
        if mx < dp[i]:
            ans = [i]
            mx = dp[i]
        elif mx == dp[i]:
            ans.append(i)
    elif not dp[i]:
        find(i)
print(dp)
print(*ans)