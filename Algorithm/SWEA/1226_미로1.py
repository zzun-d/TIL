def search(x ,y):
    global flag
    for dx, dy in move:
        nx = dx + x
        ny = dy + y
        if 0 < nx < 16 and 0 < ny < 16 and maze[nx][ny] == 0 and (nx, ny) not in visited:
            visited.append((nx, ny))
            search(nx, ny)
        elif maze[nx][ny] == 3:
            flag = 1
    
for _ in range(10):
    flag = 0
    visited = []
    t= int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    search(1, 1)
    print(f'#{t} {flag}')