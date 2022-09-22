R, C, N = map(int, input().split())
arr = [input() for _ in range(R)]
bomb = [[-1]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            bomb[i][j] = 3

for n in range(N):

    if n % 2:
        for i in range(R):
            for j in range(C):
                if bomb[i][j] < 0:
                    bomb[i][j] = 3
                else:
                    bomb[i][j] -= 1

    else:
        for i in range(R):
            for j in range(C):
                if bomb[i][j] > 0:
                    bomb[i][j] -= 1
                    if bomb[i][j] == 0:
                        bomb[i][j] = -1
                        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ni = i + di
                            nj = j + dj
                            if 0 <= ni < R and 0 <= nj < C:
                                bomb[i][j] = -1
print(bomb)
# for i in range(R):
#     row = ''
#     for j in range(C):
#         if bomb[i][j] < 0:
