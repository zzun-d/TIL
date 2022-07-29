a, b = map(int, input().split())

robot_map = [list(input()) for _ in range(a)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
d = ['>', '<', 'v', '^']

d_init = None
def search_way(x, y):
    global d_init
    possible_way = []
    for d_x, d_y, _d in zip(dx, dy, d):
        nx = x + d_x
        ny = y + d_y
        
        if 0 <= nx < b and 0 <= ny < a and robot_map[nx][ny] == '#':
            possible_way.append(_d)

    if len(possible_way) == 1:
        d_init = possible_way[0]
        return True
    
def go_way(x, y):
    for d_x, d_y in zip(dx, dy):
        nx = x + d_x
        ny = y + d_y
        if 0 <= nx < b and 0 <= ny < a and robot_map[nx][ny] == '#':
            return

tmp = 0
for i in range(a):
    for j in range(b):
        if robot_map[i][j] == '#' and search_way(i, j):
            x, y = (i, j)
            tmp = 1
            break
    if tmp:
        break
    
print(x+1, y+1)
print(d_init)

