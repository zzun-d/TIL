def f(n, k, c):
    global cnt
    if c == N and k == K:
        cnt += 1
        return
    elif n > 12:
        return
    elif c >= N:
        return

    f(n+1, k+n, c+1)
    f(n+1, k, c)
    
        
        
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    f(1, 0, 0)
    print(f'#{tc} {cnt}')