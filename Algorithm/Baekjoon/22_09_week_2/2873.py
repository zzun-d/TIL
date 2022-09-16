di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
dalpha = 'LDRU'
R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
visited[0][0] = True
result = ''
mx_enjoy = 0

if R%2:
    result += 'R'*(C-1)
    for i in range(R-1):
        result += 'D'
        if i%2:
            result += 'R'*(C-1)
        else:
            result += 'L'*(C-1)
elif C%2:
    result += 'D'*(R-1)
    for i in range(C-1):
        result += 'R'
        if i%2:
            result += 'D'*(R-1)
        else:
            result += 'U'*(R-1)
else:
    mn = 1000
    mi, mj = (1, 1)
    for i in range(R):
        for j in range(C):
            if arr[i][j] < mn and (i+j)%2:
                mn = arr[i][j]
                mi, mj = i, j
    visited[mi][mj] = True
    result = ''
    for _ in range(mj//2):
        result += 'D' * (R-1) + 'R' + 'U' * (R-1) + 'R'
    if mj%2:
        y = mj - 1

    else:
        y = mj
    x = 0
    while True:
        if (x, y+1) == (mi, mj):
            x += 1
            result += 'D'
        y += 1
        result += 'R'
        if x == R-1:
            break
        x += 1
        result += 'D'
        if x == R-1:
            break

        if (x, y-1) == (mi, mj):
            x += 1
            result += 'D'

        y -= 1
        result += 'L'

        x += 1
        result += 'D'
    while (x, y) != (R-1, C-1):
        y += 2
        result += 'R' + 'U'*(R-1) + 'R' + 'D'*(R-1)

print(result)