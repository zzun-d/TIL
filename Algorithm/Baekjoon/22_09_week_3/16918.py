R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
bomb = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            bomb.append((i, j))

if N <= 1:
    for i in range(R):
        print(''.join(arr[i]))

elif not N%2:
    for _ in range(R):
        print('O'*C)
else:
    if N % 4 == 3:
        arr = [['O']*C for _ in range(R)]
        for i, j in bomb:
            arr[i][j] = '.'
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    arr[ni][nj] = '.'
        for i in range(R):
            print(''.join(arr[i]))
    
    else:
        arr = [['O']*C for _ in range(R)]
        for i, j in bomb:
            arr[i][j] = '.'
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    arr[ni][nj] = '.'
        bomb = []
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    bomb.append((i, j))
        arr = [['O']*C for _ in range(R)]
        for i, j in bomb:
            arr[i][j] = '.'
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    arr[ni][nj] = '.'
        for i in range(R):
            print(''.join(arr[i]))
        
