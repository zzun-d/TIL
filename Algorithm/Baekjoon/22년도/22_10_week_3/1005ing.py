from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip()


def search(n):

    for i in graph_re[n]:
        if not dp[i]:
            dp[i] = costs[i]
        else:
            dp[i] = max(dp[i], dp[n]+costs[i])        
       

    
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    costs = [0] + list(map(int, input().split()))
    graph = defaultdict(list)
    graph_re = defaultdict(list)
    dp = [0]*(N+1)
    for _ in range(K):
        p, c = map(int, input().split())
        graph[c].append(p)
        graph_re[p].append(c)
    target = int(input())
    
    basic = set(range(1, N+1)) - set(graph.keys())
    for i in basic:
        dp[i] = costs[i]
    for i in basic:
        search(i)

    print(dp)