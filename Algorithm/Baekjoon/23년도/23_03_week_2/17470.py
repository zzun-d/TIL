import sys

def input():
    return sys.stdin.readline().rstrip()

def turn_cal(o):
    if o == '1':
        state[0] = not state[0]
        arr_idx[0], arr_idx[1], arr_idx[2], arr_idx[3] = arr_idx[3], arr_idx[2], arr_idx[1], arr_idx[0]
    elif o == '2':
        state[1] = not state[1]
        arr_idx[0], arr_idx[1], arr_idx[2], arr_idx[3] = arr_idx[1], arr_idx[0], arr_idx[3], arr_idx[2]
    elif o == '3':
        if state[2]:
            state[0] = not state[0]
            state[1] = not state[1]
            state[2] = not state[2]
        else:
            state[2] = not state[2]
        arr_idx[0], arr_idx[1], arr_idx[2], arr_idx[3] = arr_idx[3], arr_idx[0], arr_idx[1], arr_idx[2]
    elif o == '4':
        if not state[2]:
            state[0] = not state[0]
            state[1] = not state[1]
            state[2] = not state[2]
        else:
            state[2] = not state[2]
        arr_idx[0], arr_idx[1], arr_idx[2], arr_idx[3] = arr_idx[1], arr_idx[2], arr_idx[3], arr_idx[0]

    elif o == '5':
        arr_idx[0], arr_idx[1], arr_idx[2], arr_idx[3] = arr_idx[3], arr_idx[0], arr_idx[1], arr_idx[2]

    else:
        arr_idx[0], arr_idx[1], arr_idx[2], arr_idx[3] = arr_idx[1], arr_idx[2], arr_idx[3], arr_idx[0]

def turn(state, arr):
    if state[0]:
        arr = up_down(arr)
    if state[1]:
        arr = left_right(arr)
    if state[2]:
        arr = rotate(arr)
    return arr
        
def arr_sum(arr, out_num):
    d_i = d_j = 0
    m = M
    n = N
    
    if state[2]:
        m, n = n, m
        
    if out_num%4 == 1:
        d_j = m//2
    elif out_num%4 == 2:
        d_i = n//2
        d_j = m//2
    elif out_num%4 == 3:
        d_i = n//2

    for i in range(n//2):
        for j in range(m//2):
            ans[i+d_i][j+d_j] = arr[i][j]

def left_right(arr):
    for i in range(N//2):
        for j in range(M//4):
            arr[i][j], arr[i][-1-j] = arr[i][-1-j], arr[i][j]
    return arr

def up_down(arr):
    for i in range(N//4):
        for j in range(M//2):
            arr[i][j], arr[-1-i][j] = arr[-1-i][j], arr[i][j]
    return arr

def rotate(arr):
    
    new_arr = [[0]*(N//2) for _ in range(M//2)]
    for i in range(M//2):
        for j in range(N//2):
            new_arr[i][N//2-j-1] = arr[j][i]
    
    return new_arr
    


N, M, R = map(int, input().split())
arr = [input().split() for _ in range(N)]

arr_idx = [0, 1, 2, 3]

arr0 = [[arr[i][j] for j in range(M//2)] for i in range(N//2)]
arr1 = [[arr[i][j+M//2] for j in range(M//2)] for i in range(N//2)]
arr2 = [[arr[i+N//2][j+M//2] for j in range(M//2)] for i in range(N//2)]
arr3 = [[arr[i+N//2][j] for j in range(M//2)] for i in range(N//2)]
oper = input().split()
state = [False, False, False, 0]

for o in oper:
    turn_cal(o)
print(state)
if state[2]:
    ans = [[0]*N for _ in range(M)]
else:
    ans = [[0]*M for _ in range(N)]

real_idx = [0, 0, 0, 0]
for i, a in enumerate(arr_idx):
    real_idx[a] = i

arr_sum(turn(state, arr0), real_idx[0])
arr_sum(turn(state, arr1), real_idx[1])
arr_sum(turn(state, arr2), real_idx[2])
arr_sum(turn(state, arr3), real_idx[3])

for row in ans:
    print(*row)
