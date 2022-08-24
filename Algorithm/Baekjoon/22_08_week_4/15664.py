N, M = map(int, input().split())
l = list(map(int, input().split()))

result = []
visited = [False] * N


def dfs(lst, c):

    if c == M:
        result.append(tuple(lst))
        return

    for i in range(N):
        if not visited[i]:
            if lst:
                if lst[-1] > l[i]:
                    continue
                lst.append(l[i])
            else:
                lst = [l[i]]

            visited[i] = True
            dfs(lst, c+1)
            lst.pop()
            visited[i] = False


dfs([], 0)

result = list(set(result))
result.sort()
for r in result:
    print(*r)