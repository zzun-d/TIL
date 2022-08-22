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

