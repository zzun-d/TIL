def f(n, lst):
    global tmp
    if n==6:
        if (lst[0]+2 == lst[1]+1 == lst[2] or lst[0] == lst[1] == lst[2]) and (lst[3]+2 == lst[4]+1 == lst[5] or lst[3] == lst[4] == lst[5]):
            tmp = 1
            return
    else:
        for i in range(6):
            if visited[i] == 0:
                visited[i] = 1
                f(n+1, lst + prob[i:i+1])
                visited[i] = 0



T = int(input())
for tc in range(1, T+1):
    prob = list(map(int, list(input())))
    visited = [0]*6
    tmp = 0
    f(0, [])
    print(f'#{tc} {tmp}')