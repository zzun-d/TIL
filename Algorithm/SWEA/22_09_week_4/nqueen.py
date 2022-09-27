def n_queen(i):
    global cnt

    if i >= N:
        cnt += 1
        return

    for j in range(1, N+1):
        if j not in visited:
            for k in range(i):
                if i-k == abs(visited[k]-j):
                    break
            else:
                visited[i] = j
                n_queen(i+1)
                visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    visited = [0]*N
    n_queen(0)
    print(f'#{tc} {cnt}')