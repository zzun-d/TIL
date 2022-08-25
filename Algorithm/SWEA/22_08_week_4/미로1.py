for _ in range(10):
    t = input()
    arr = [input() for _ in range(16)]

    for i in range(16):
        tmp = 0
        for j in range(16):
            if arr[i][j] == '2':
                si, sj = i, j
                tmp = 1
                break
        if tmp:
            break

    queue = [(si, sj)]
    v = [[0]*16 for _ in range(16)]
    v[si][sj] = 1
    ans = 0
    while queue:
        i, j = queue.pop(0)

        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and not v[ni][nj] and arr[ni][nj] != '1':
                v[ni][nj] = 1
                queue.append((ni, nj))
                if arr[ni][nj] == '3':
                    ans = 1
                    queue = False
                    break
    print(f'#{t} {ans}')
