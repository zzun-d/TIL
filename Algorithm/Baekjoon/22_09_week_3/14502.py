from collections import deque

def count_safe():

    cnt = 0
    queue = deque(virus[:])
    visited = [[0]*M for _ in range(N)]
    for i, j in queue:
        visited[i][j] = 1
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
                    cnt += 1
    return cnt
    



def stand_wall(i, j, k):
    global mx_safe
    
    if k == 3:
        mx_safe = min(mx_safe, count_safe())
    elif j == M:
        i += 1
        j = 0
        stand_wall(i, j, k)
    elif i == N:
        return
    
    else:
        if arr[i][j] == 0:
            arr[i][j] = 1
            stand_wall(i, j+1, k+1)
            arr[i][j] = 0
        stand_wall(i, j+1, k)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
safe_area = -3
mx_safe = N*M
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        elif arr[i][j] == 0:
            safe_area += 1
stand_wall(0, 0, 0)
print(safe_area - mx_safe)
