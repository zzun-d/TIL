def inord(n):
    global cnt

    if n <= N:
        inord(n*2)
        lst[n] = cnt
        cnt += 1
        inord(n*2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0]*(N+1)
    cnt = 1
    inord(1)

    print(f'#{tc} {lst[1]} {lst[N//2]}')