def f(n, sm):
    global mn
    if n >= N:
        mn = min(mn, sm)
        return
    if sm > mn:
        return
        
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            f(n+1, sm+arr[n][i])
            visited[i] = 0
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    mn = 100
    f(0, 0)
    print(f'#{tc} {mn}')