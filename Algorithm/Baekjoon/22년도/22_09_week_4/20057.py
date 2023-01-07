import sys

def input():
    return sys.stdin.readline().rstrip()

def tornado(x, y, turn):
    global out_sand
    sand = arr[x][y]
    used_sand = 0
    arr[x][y] = 0
    if turn:
        for i in range(10):
            D[i][1], D[i][2] = -D[i][2], D[i][1]

    if sand < 10:
        if 0 <= x + D[-1][1] < N and 0 <= y + D[-1][2] < N:
            arr[x + D[-1][1]][y + D[-1][2]] += sand
        else:
            out_sand += sand
    else:
        for ratio, dx, dy in D:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if ratio == 1:
                    arr[nx][ny] += int(sand - used_sand)
                else:
                    arr[nx][ny] += int(ratio * sand)
                    used_sand += int(ratio * sand)
            else:

                if ratio == 1:
                    out_sand += int(sand - used_sand)
                else:
                    used_sand += int(ratio * sand)
                    out_sand += int(ratio*sand)

D = [[0.01, -1, 1], [0.01, 1, 1], [0.02, -2, 0], [0.02, 2, 0], [0.05, 0, -2], [0.07, -1, 0], [0.07, 1, 0], [0.1, -1, -1], [0.1, 1, -1], [1, 0, -1]]
T = [(0, -1), (1, 0), (0, 1), (-1, 0)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
si = N//2
sj = N//2 - 1
out_sand = 0
length = 1
move = 0
tmp = 2
turn = False
t = 0
while si or sj != -1:
    tornado(si, sj, turn)

    move += 1

    if length == move:
        t = (t+1) % 4
        turn = True
        move = 0
        tmp -= 1
    else:
        turn = False
    if not tmp:
        length += 1
        tmp = 2
    si += T[t][0]
    sj += T[t][1]
print(out_sand)
