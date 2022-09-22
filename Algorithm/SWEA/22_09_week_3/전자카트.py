def f(r, sm, k):
    global mn
    if k == N:
        mn = min(mn, sm)

    else:
        for i in range(N):
            if not visited_c[i] and not visited_r[r]:
                visited_c[i] = visited_r[r] = 1
                f(i, sm + arr[r][i], k+1)
                visited_c[i] = visited_r[r] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mn = 1000
    visited_r = [0] * N
    visited_c = [0] * N
    f(0, 0, 0)
    print(f'#{tc} {mn}')