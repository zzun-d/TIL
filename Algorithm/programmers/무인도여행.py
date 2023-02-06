from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    arr = [list(maps[i]) for i in range(N)]
    
    answer = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'X':
                continue
            cnt = int(arr[i][j])
            arr[i][j] = 'X'
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx = x + dx
                    ny = y + dy
                    
                    if N > nx >= 0 and M > ny >= 0 and arr[nx][ny] != 'X':
                        cnt += int(arr[nx][ny])
                        arr[nx][ny] = 'X'
                        q.append((nx, ny))     
            answer.append(cnt)
            
    if not answer:
        return [-1]
    return sorted(answer)