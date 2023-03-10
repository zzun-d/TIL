import sys

def input():
    return sys.stdin.readline().rstrip()

def turn_cal(o):
    if o == '1':
        state[0] = ~state[0]
    elif o == '2':
        state[1] = ~state[1]
    elif o == '3':
        if state[2]:
            state[0] = ~state[0]
            state[1] = ~state[1]
            state[2] = ~state[2]
        else:
            state[2] = ~state[2]
        state[3] += 1

    elif o == '4':
        if not state[2]:
            state[0] = ~state[0]
            state[1] = ~state[1]
            state[2] = ~state[2]
        else:
            state[2] = ~state[2]
        state[3] -= 1
    
    elif o == '5':
        state[3] += 1
    else:
        state[3] -= 1

def turn(s1, s2, s3, arr):
    if s1:
        arr = left_right(arr)
    if s2:
        arr = up_down(arr)
    if s3:
        arr = rotate(arr)
    return arr
        
def arr_sum(arr, out_num):
    d_i = d_j = 0
    
    if out_num == 1:
        d_j = N//2
    elif out_num == 2:
        d_i = N//2
        d_j = N//2
    elif out_num == 3:
        d_i = N//2
    
    for i in range(N//2):
        for j in range(M//2):
            ans[i+d_i][j+d_j] = arr[i][j]

def left_right(arr):
    for i in range(N//4):
        for j in range(M//4):
            arr[i][j], arr[i][-1-j] = arr[i][-1-j], arr[i][j]
    return arr

def up_down(arr):
    for i in range(N//4):
        for j in range(M//4):
            arr[i][j], arr[-1-i][j] = arr[-1-i][j], arr[i][j]
    return arr

def rotate(arr):
    new_arr = [[0]*N//2 for _ in range(M//2)]
    
    


N, M, R = map(int, input().split())
arr = [input().split() for _ in range(N)]

arr0 = [[arr[i][j] for j in range(M//2)] for i in range(N//2)]
arr1 = [[arr[i][j+M//2] for j in range(M//2)] for i in range(N//2)]
arr2 = [[arr[i+N//2][j+M//2] for j in range(M//2)] for i in range(N//2)]
arr3 = [[arr[i+N//2][j] for j in range(M//2)] for i in range(N//2)]

oper = input().split()
state = [False, False, False, 0]

for o in oper:    
    turn_cal(o)
state[3] = abs(state[3])%4


ans = [[0]*M for _ in range(N)]






print(ans)