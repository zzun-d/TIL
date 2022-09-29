from collections import defaultdict, deque


def dfs(node):
    stack = [node]
    visited = [0] * (N + 1)
    visited[V] = 1
    path = [node]
    while stack:
        n = stack[-1]
        for i in sorted(graph[n]):
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                path.append(i)
                break
        else:
            stack.pop()
    print(*path)

N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans1 = False
ans2 = [V]

stack = [V]
dfs(V)
visited = [0]*(N+1)
visited[V] = 1
queue = deque([V])
while queue:
    v = queue.popleft()
    for i in sorted(graph[v]):
        if not visited[i]:
            visited[i] = 1
            queue.append(i)
            ans2.append(i)

print(*ans2)

