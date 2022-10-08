T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    tree = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    visited[1] = 1
    ans = [1]
    stack = [1]

    for _ in range(E):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    while stack:
        n = stack[-1]
        for i in sorted(tree[n]):
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                ans.append(i)
                break
        else:
            stack.pop()
    print(f'#{tc}', *ans)