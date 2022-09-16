import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
water = deque([])

for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            water.append((i, j))
        elif arr[i][j] == 'S':
            S = (i, j)

queue_s = deque([S])

cnt = 0
tmp = False
while queue_s:
    cnt += 1
    for _ in range(len(water)):
        i, j = water.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] in ['S', '.']:
                water.append((ni, nj))
                arr[ni][nj] = '*'

    for _ in range(len(queue_s)):
        i, j = queue_s.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] == '.':
                    queue_s.append((ni, nj))
                    arr[ni][nj] = '*'
                elif arr[ni][nj] == 'D':
                    tmp = True
                    break
        if tmp:
            break
    if tmp:
        break

if tmp:
    print(cnt)
else:
    print('KAKTUS')

