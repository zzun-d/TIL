def f(i, p):
    global mx
    if p <= mx:
        return
    if i >= N:
        mx = max(mx, p)
        return
    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            f(i+1, p*arr[i][j]/100)
            visited[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    mx = 0
    f(0, 100)
    print(f'# {mx:6f}')