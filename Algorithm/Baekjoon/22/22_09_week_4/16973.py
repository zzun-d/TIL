from collections import deque


def check_wall(x, y, dx):
    if dx == 1:
        if sum(arr[x+H-1][y:y+W]):
            return False
        return True
    elif dx == -1:
        if sum(arr[x][y:y+W]):
            return False
        return True
    else:
        for i in range(x, x+H):
            if arr[i][y] or arr[i][y+W-1]:
                return False
        return True    


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1
queue = deque([(Sr, Sc)])
visited = [[0]*M for _ in range(N)]
tmp = True
cnt = 0
while queue and tmp:
    cnt += 1
    for _ in range(len(queue)):
        i, j = queue.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni <= N-H and 0 <= nj <= M-W and not visited[ni][nj] and check_wall(ni, nj, di):
                visited[ni][nj] = 1
                queue.append((ni, nj))
                if ni == Fr and nj == Fc:
                    tmp = False
                    break
        if not tmp:
            break
if tmp:
    print(-1)
else:
    print(cnt)