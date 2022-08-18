T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        
    S, G = map(int, input().split())

    stack = []
    ans = 0
    visited = [False] * (V+1)
    visited[S] = True

    while True:
        for w in graph[S]:
            if w == G:
                ans = 1
                break

            elif not visited[w]:
                visited[w] = True
                stack.append(S)
                S = w
                break
        else:
            if stack:
                S = stack.pop()
            else:
                break
        if ans:
            break

    print(f'#{t} {ans}')


