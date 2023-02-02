from collections import defaultdict
import sys

def input():
    return sys.stdin.readline().rstrip()

def D(s, cnt):
    global ans

    visited[s] = 1

    for e, t in adj[s]:
    
        if visited[e]:
            continue
    
        cntDict[e] = [D(e, cnt), t]
        cnt += 1

    return cnt


N = int(input())

adj = defaultdict(list)

for _ in range(N-1):
    x, y, t = map(int, input().split())
    adj[x].append((y, t))
    adj[y].append((x, t))

for i in range(1, N+1):
    cntDict = defaultdict(list)
    visited = [0]*(N+1)
    ans = 0
    D(i, 1)
    print(cntDict)