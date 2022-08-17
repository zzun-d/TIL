T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    stack = []
    visited = [False] * (V+1)
    adjList = [[] for _ in range(V+1)]
    ans = []
    for _ in range(E):
        s, e = map(int, input().split())
        adjList[s].append(e)
        adjList[e].append(s)
    v = 1
    ans.append(v)
    visited[v] = True
    while True:

        for w in adjList[v]:
            if not visited[w]:
                stack.append(v)
                ans.append(w)
                v = w
                visited[w] = True
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    print(f'#{t}', *ans)
