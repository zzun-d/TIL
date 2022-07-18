from collections import deque

def search(queue):
    while len(queue):
        x, y = queue.popleft()
        for dx, dy in move:
            mx = x + dx
            my = y + dy
            if 0 <= mx < N and  0 <= my < N:
                if distance[mx][my] > road_map[mx][my] + distance[x][y]:
                    distance[mx][my] = road_map[mx][my] + distance[x][y]
                    queue.append((mx, my))
     
for T in range(int(input())):
    queue = deque()
    queue.append((0,0))
    move = [[1, 0],[-1, 0],[0, 1],[0, -1]]
    N = int(input())
    road_map = [list(map(int, list(input()))) for _ in range(N)]
    distance = [[999999999]*N for _ in range(N)]
    distance[0][0] = 0
    search(queue)
    print(f'#{T+1} {distance[N-1][N-1]}')