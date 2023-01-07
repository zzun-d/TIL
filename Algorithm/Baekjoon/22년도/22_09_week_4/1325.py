from collections import defaultdict, deque
import sys

def input():
    return sys.stdin.readline().rstrip()

def find(n):
    cnt = 1
    visited = [0]*(N+1)
    visited[n] = 1
    queue = deque([n])
    
    while queue:
        q = queue.popleft()
        for v in graph[q]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
                cnt += 1

    return cnt

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

mx = 0
ans = []
for i in range(1, N+1):
    cnt = find(i)
    if cnt > mx:
        mx = cnt
        ans = [i]
    elif cnt == mx:
        ans.append(i)

print(*ans)