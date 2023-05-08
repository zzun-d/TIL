import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def find_tera():
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'T':
                si, sj = i, j
                arr[i].replace('T', '0')
                cnt += 1
            elif arr[i][j] == 'E':
                ei, ej = i, j
                cnt += 1
            if cnt >= 2:
                return si, sj, ei, ej

def sliding(x, y, i):
    D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    t = 0
    while True:
        x += D[i][0]
        y += D[i][1]
        if H > x >=0 and W > y >= 0:
            if arr[x][y].isdigit():
                t += int(arr[x][y])
            elif arr[x][y] == 'R':
                return x-D[i][0], y-D[i][1], t
            elif arr[x][y] == 'E':
                return x, y, t
            else:
                return False
        else:
            return False

W, H = map(int, input().split())
arr = [input() for _ in range(H)]
INF = 500*500*9
dijk = [[INF for _ in range(W)] for _ in range(H)]
si, sj, ei, ej = find_tera()
dijk[si][sj] = 0

q = deque([(si, sj)])

while q:
    x, y = q.popleft()
    for i in range(4):
        info = sliding(x, y, i)
        if info:
            nx, ny, t = info
            if dijk[nx][ny] > dijk[x][y] + t:
                dijk[nx][ny] = dijk[x][y] + t
                q.append((nx, ny))

if dijk[ei][ej] >= INF:
    print(-1)
else:
    print(dijk[ei][ej])