def dfs(n, i):
    if len(n) == M:
        ans.append(n)
        return
    elif i == N:
        return

    dfs(n + [lst[i]], i+1)
    dfs(n, i+1)

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
ans = []

dfs([], 0)
ans.sort()

for a in ans:
    print(*a)