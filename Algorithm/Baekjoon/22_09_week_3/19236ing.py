import copy

def fish_move(arr1, arr2):
    for i in range(1, 17):
        if arr1[fish_dict[i][0]][fish_dict[i][1]] > 0:
            x, y = fish_dict[i]
            d = arr2[x][y]
            for _ in range(8):
                nx = x + D[d][0]
                ny = y + D[d][1]
                if 0 <= nx < 4 and 0 <= ny < 4 and arr1[nx][ny] >= 0:
                    for k in fish_dict.keys():
                        fi, fj = fish_dict[k]
                        if fi == nx and fj == ny:
                            fish_dict[i], fish_dict[k] = fish_dict[k], fish_dict[i]
                            break
                    arr1[x][y], arr1[nx][ny] = arr1[nx][ny], arr1[x][y]
                    arr2[x][y], arr2[nx][ny] = arr2[nx][ny], arr2[x][y]

                    break
                else:
                    d = (d+1) % 8

def shark_move(x, y, f, ar1, ar2):
    global mx_fd
    if not ar1[x][y]:
        return
    mx_fd = max(mx_fd, f)
    f += ar1[x][y]
    ar1[x][y] = -1

    fish_move(ar1, ar2)
    d = ar2[x][y]
    k = 1
    while True:
        nx = x + D[d][0]*k
        ny = y + D[d][1]*k
        if 0 <= nx < 4 and 0 <= ny < 4:
            ar1[x][y] = 0
            shark_move(nx, ny, f, copy.deepcopy(ar1), copy.deepcopy(ar2))
            k += 1
            ar1[x][y] = -1
        else:
            break

D = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
arr1 = [[0]*4 for _ in range(4)]
arr2 = [[0]*4 for _ in range(4)]
fish_dict = {}
for i in range(4):
    info = list(map(int, input().split()))

    for idx, j in enumerate(range(0, 8, 2)):
        arr1[i][idx] = info[j]
        fish_dict[info[j]] = (i, idx)
        arr2[i][idx] = info[j+1] - 1

mx_fd = 0
shark_move(0, 0, 0, arr1, arr2)
print(mx_fd)