T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << N):
        s_sum = 0
        for j in range(N):
            if i & (1 << j):
                s_sum += lst[j]
            if s_sum > K:
                break
        if s_sum == K:
            cnt += 1

    print(f'#{t} {cnt}')









def dfs(n, sm):
    global ans

    # 가지치기는 제일 위에서, 마지막 순서로
    if sm > K:
        return

    # 종료조건
    if n == N:
        if sm == K:
            ans += 1
        return
   
    dfs(n+1, sm+lst[n]) # 사용하는 경우
    dfs(n+1, sm)        # 사용하지 않는 경우



T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0

    dfs(0, 0)

    print(f'#{t} {ans}')