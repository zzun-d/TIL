def dfs(n, d, x, y):
    global cost
    if cost < d:
        return
    if n == N:
        d += abs(x - end_coordi[0]) + abs(y - end_coordi[1])
        cost = min(cost, d)
        return
    for i in range(N):
        if need_visit[i]:
            need_visit[i] = False
            u_d = d + abs(x - client_coordi[i][0]) + abs(y - client_coordi[i][1])
            dfs(n+1, u_d, client_coordi[i][0], client_coordi[i][1])
            need_visit[i] = True

T = int(input())
for t in range(T):
    N = int(input())
    coordi = list(map(int, input().split()))
    start_coordi = (coordi.pop(0), coordi.pop(0))
    end_coordi = (coordi.pop(0), coordi.pop(0))
    client_coordi = []
    need_visit = [True] * N
    cost = 2000
    for i in range(N):
        client_coordi.append((coordi[i*2], coordi[i*2+1]))
    dfs(0, 0, start_coordi[0], start_coordi[1])

    print(f'#{t+1} {cost}')