from collections import defaultdict, deque

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
                mi, mj = [i, j]
    visited[mi][mj] = True:
    stack = [(0, 0)]
    path = []
    while stack:
        if stack[-1] == (R-1, C-1):
            break

print(result)


