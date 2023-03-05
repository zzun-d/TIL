R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

def build(x, y):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if arr[nx][ny] == 'W':
                return False

            elif arr[nx][ny] != 'S':
                arr[nx][ny] = 'D'
    return True
tmp = True
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            tmp = build(i, j)
        if not tmp:
            break
    if not tmp:
        break
if not tmp:
    print(0)
else:
    print(1)
    for a in arr:
        print(''.join(a))
