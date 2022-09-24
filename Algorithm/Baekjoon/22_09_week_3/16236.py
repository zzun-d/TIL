from collections import deque

def bfs(x, y):
    global tmp, nd, s
    queue = deque([(x, y)])
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    cnt = 0
    target = 0

    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < s:
                target += 1
                break
        else:
            continue
        break
    if not target:
        tmp = False
        return
    while queue:
        cnt += 1
        fishes = []
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] <= s:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                    if 0 < arr[ni][nj] < s:
                        fishes.append((ni, nj))
        if fishes:
            break

    if fishes:
        i = j = N
        for fi, fj in fishes:
            if fi < i:
                i = fi
                j = fj
            elif fi == i and fj < j:
                j = fj
        arr[i][j] = 0
        if nd == 1:
            s += 1
            nd = s
        else:
            nd -= 1

        return cnt, i, j

    tmp = False
    return
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si = i
            sj = j
            arr[i][j] = 0
            break

tmp = True
nd = 2
s = 2
t = 0
while tmp:
    value = bfs(si, sj)
    if value:
        tt, si, sj = value
        t += tt
print(t)
