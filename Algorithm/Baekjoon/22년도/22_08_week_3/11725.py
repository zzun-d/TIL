import sys

input = sys.stdin.readline

N = int(input())
adjList = [[] for _ in range(100001)]
for _ in range(1, N):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

ans = [0]*(N+1)
need_visit = [1]

while need_visit:
    nxt_visit = []
    for node in need_visit:
        for i in adjList[node]:
            if not ans[i]:
                ans[i] = node
                nxt_visit.append(i)
    need_visit = nxt_visit        
for i in ans[2:]:
    print(i) 