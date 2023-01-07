from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def search(i, j):
    # print(i, j)
    # print(arr)
    # print(visited)
    for d in range(4):
        ni = i +di[d]
        nj = j +dj[d]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(arr[i][j] - arr[ni][nj]) <= R:
            united.append((ni, nj))
            visited[ni][nj] = 1
            search(ni, nj)
        
cnt = 0
while True:
    uniteds = []
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print(i, j)
            # print(cnt)
            united = [(i, j)]
            if not visited[i][j]:
                visited[i][j] = 1
                search(i, j)
            if len(united) > 1:
                uniteds.append(united)
            # print('---------------------')
            # print(united)
            # print('---------------------')
    
    if uniteds:
        for united in uniteds:
            l = len(united)
            sm = sum([arr[i][j] for i, j in united])
            aver = sm // l
            for i, j in united:
                arr[i][j] = aver
    else:
        break
    cnt += 1

print(cnt)