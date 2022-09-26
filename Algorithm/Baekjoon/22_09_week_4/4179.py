from collections import deque


def move():
    global f_lst
    cnt = 0
    while f_lst:
        cnt += 1
        nxt = {}
        check_lst = []
        for _ in range(len(f_lst)):
            i, j, t = f_lst.pop()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:

                    if t > 0:
                        visited[ni][nj] = 1
                        if not nxt.get((ni, nj)):
                            nxt[(ni, nj)] = (ni, nj, 1)
                            if ni == 0 or nj == 0 or ni == R-1 or nj == C-1:
                                check_lst.append((ni, nj))
                    else:
                        visited[ni][nj] = -1
                        if not nxt.get((ni, nj)) or nxt.get((ni, nj)) == (ni, nj, 1):
                            nxt[(ni, nj)] = (ni, nj, -1)
        for i, j in check_lst:
            if nxt[(i, j)] == (i, j, 1):
                cnt += 1
                return cnt
        f_lst = list(nxt.values())
        
    return 'IMPOSSIBLE'


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
f_lst = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '.':
            continue
        elif arr[i][j] in ['#', 'F']:
            visited[i][j] = -1
            if arr[i][j] == 'F':
                f_lst.append((i, j, -1))
        else:
            f_lst.append((i, j, 1))

ans = move()
print(ans)

