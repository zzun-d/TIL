def dfs(n, m, v):
    global sm
    if m >= sm:
        return

    if n == N:
        if sm > m:
            sm = m
        return

    for i in range(N):
        if i not in v:
            dfs(n+1, m+arr[n][i], v+[i])

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sm = 100
    dfs(0, 0, [])

    print(f'#{t} {sm}')
