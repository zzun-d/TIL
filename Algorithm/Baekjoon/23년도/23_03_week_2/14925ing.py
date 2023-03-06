def search(x, y):
    d = 1
    # print(x, y)
    # print(d)
    while d < M-x and d < N-y:
        for i in range(d+1):
            if arr[x+i][y+d]:
                return d
        for i in range(d):
            if arr[x+d][y+i]:
                return d
        d += 1
    return d-1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
x = y = 0
while x <= M - cnt:
    if y >= N - cnt:
        x += 1
        y = 0
        continue
    if arr[x][y] < 0:
        y += 1
        continue
    else:
        cnt = max(cnt, search(x, y))
        y += 1

print(cnt)