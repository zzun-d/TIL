from collections import defaultdict, deque


def dfs(n, path):
    global ans1
    if len(path) == N:
        print(*path)
        ans1 = True
        return
    else:
        for i in sorted(graph[n]):
            if ans1:
                break
            if not visited[i]:
                visited[i] = 1
                dfs(i, path+[i])
                visited[i] = 0

N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans1 = False
ans2 = [V]
visited = [0]*(N+1)
visited[V] = 1
dfs(V, [V])
visited = [0]*(N+1)
visited[V] = 1
queue = deque([V])
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            queue.append(i)
            ans2.append(i)

print(*ans2)