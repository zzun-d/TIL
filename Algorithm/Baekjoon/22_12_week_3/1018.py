def compair(chess, b_x, b_y, x, y, cnt):
    if cnt >= mn_cnt:
        return 64
    elif y == 8:
        return compair(chess, b_x+1, b_y-8, x+1, 0, cnt)
    elif x == 8:
        return cnt
    elif chess[x][y] != arr[b_x][b_y]:
        return compair(chess, b_x, b_y+1, x, y+1, cnt+1)
    else:
        return compair(chess, b_x, b_y+1, x, y+1, cnt)
    

N, M = map(int ,input().split())
arr = [input() for _ in range(N)]
chess_1 = ['WBWBWBWB', 'BWBWBWBW']*4
chess_2 = ['BWBWBWBW', 'WBWBWBWB']*4
mn_cnt = 64
for i in range(N-7):
    for j in range(M-7):
        for chess in [chess_1, chess_2]:
            mn_cnt = min(mn_cnt, compair(chess, i, j, 0, 0, 0))
print(mn_cnt)