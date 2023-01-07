from collections import deque

def find(i, j):
    q =deque([i])
    visited = [0]*N
    while q:
        ni = q.popleft()
        for k in range(N):
            if arr[ni][k] == 1 and visited[k] == 0:
                visited[k] = 1
                if k == j:
                    n_arr[i][j] = 1
                    return
                q.append(k)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
n_arr = [[0]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        find(x, y)
        
for l in n_arr:
    print(*l)