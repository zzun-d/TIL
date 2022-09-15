T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        l, v = map(int, input().split())
        tree[l] = v
    for i in range(N, 1, -1):
        if not i%2:
            if i+1 <= N:
                tree[i//2] = tree[i]+tree[i+1]
            else:
                tree[i//2] = tree[i]

    print(f'#{tc} {tree[L]}')