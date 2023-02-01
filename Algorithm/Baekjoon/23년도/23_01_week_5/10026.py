import sys

sys.setrecursionlimit(10**6)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited_n = [[0]*N for _ in range(N)]
visited_r = [[0]*N for _ in range(N)]
visited_r[0][0] = 1
cnt_n = cnt_r = 0
def search_n(x, y):
    visited_n[x][y] = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if N > nx >= 0 and N > ny >= 0 and arr[x][y] == arr[nx][ny] and visited_n[nx][ny] == 0:
            search_n(nx, ny)

def search_r(x, y):
    visited_r[x][y] = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if N > nx >= 0 and N > ny >= 0 and (arr[x][y] == arr[nx][ny] or (arr[x][y] in ["R", "G"] and arr[nx][ny] in ["R", "G"])) and visited_r[nx][ny] == 0:
            search_r(nx, ny)

for i in range(N):
    for j in range(N):
        if visited_n[i][j]:
            continue
        cnt_n += 1
        search_n(i, j)

for i in range(N):
    for j in range(N):
        if visited_r[i][j]:
            continue
        cnt_r += 1
        search_r(i, j)

print(cnt_n, cnt_r)