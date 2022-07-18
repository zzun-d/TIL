T = int(input())
for i in range(T):
    answer = 0
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for j in range(N)]
    state_row = []
    state_col = []
    for j in range(N):
        s_row = 0
        s_col = 0
        for k in range(N):
            if puzzle[j][k] == 1:
                s_row += 1
            else:
                state_row.append(s_row)
                s_row = 0
        if s_row != 0:
            state_row.append(s_row)
    for j in range(N):
        s_row = 0
        s_col = 0
        for k in range(N):
            if puzzle[k][j] == 1:
                s_col += 1
            else:
                state_col.append(s_col)
                s_col = 0
        if s_col != 0:
            state_col.append(s_col)
    for j in state_row:
        if j == K:
            answer += 1
    for j in state_col:
        if j == K:
            answer += 1
    print(f'#{i+1} {answer}')
            