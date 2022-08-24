N, M = map(int, input().split())
l = list(map(int, input().split()))

result = []


def dfs(lst, c):

    if c == M:
        result.append(tuple(lst))
        return

    for i in range(N):
        lst.append(l[i])
        dfs(lst, c+1)
        lst.pop()

dfs([], 0)

result = list(set(result))
result.sort()
for r in result:
    print(*r)