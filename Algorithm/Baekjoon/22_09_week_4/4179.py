from heapq import heappush, heappop
import sys

def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
queue = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'F':
            heappush(queue, (0, i, j))

        elif arr[i][j] == 'J':
            heappush(queue, (1, i, j))
            si = i
            sj = j

cnt = 0
tmp = True
if si == 0 or si == N-1 or sj == 0 or sj == M-1:
    cnt += 1
    tmp = False

while queue and tmp:
    cnt += 1
    for _ in range(len(queue)):
        s, i, j = heappop(queue)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not s%2 and arr[ni][nj] in ['.', 'J']:
                    heappush(queue, (s+2, ni, nj))
                    arr[ni][nj] = 'F'
                elif s%2 and arr[ni][nj] == '.':
                    if ni == 0 or ni == N - 1 or nj == 0 or nj == M - 1:
                        tmp = False
                        cnt += 1
                        break
                    heappush(queue, (s+2, ni, nj))
                    arr[ni][nj] = 'J'
        if not tmp:
            break

if tmp:
    print('IMPOSSIBLE')
else:
    print(cnt)

