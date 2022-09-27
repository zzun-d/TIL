def min_cost(i, sm):
    global cost
    if sm >= cost:
        return
    if i >= N:
        cost = min(cost, sm)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            min_cost(i+1, sm+arr[i][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    cost = 1500
    min_cost(0, 0)
    print(f'#{tc} {cost}')