def search(i, j):

    for di, dj in [(1, 0),(0, -1),(-1, 0),(0, 1)]:
        ni = i + di
        nj = j + dj
        if arr[ni][nj] == 0:
            result.append((i, j))
            return

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
t = 0
result = '0'
while result:
    print(result)
    pre_cheese = len(result)
    result = []
    for i in range(1+t, R-1-t):
        for j in range(1+t, C-1-t):
            if arr[i][j] == 1:
                search(i, j)


    for i, j in result:
        arr[i][j] = 0
    t += 1

print(t-1)
print(pre_cheese)
