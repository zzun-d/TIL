T = int(input())
for t in range(T):
    sdoku_row = [input().split() for _ in range(9)]
    sdoku_col = [[sdoku_row[j][k] for j in range(9)] for k in range(9)]
    sdoku_section = [[sdoku_row[3*i + k][j + 3*l] for j in range(3) for k in range(3)] for i in range(3) for l in range(3)]
    state = 1
    for i in range(9):
        if len(set(sdoku_row[i])) != 9 or len(set(sdoku_col[i])) != 9 or len(set(sdoku_section[i])) != 9:
            print(f'#{t+1} 0')
            state = 0
            break
    if state == 1:
        print(f'#{t+1} 1')