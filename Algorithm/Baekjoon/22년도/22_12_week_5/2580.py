def impossible_check(i, j, num):
    for n in range(9):
        if arr[i][n] == num:
            return False

    for n in range(9):
        if arr[n][j] == num:
            return False

    bi = i//3 * 3
    bj = j//3 * 3
    for n in range(3):
        for m in range(3):
            if arr[bi+n][bj+m] == num:
                return False

    return True
        
tmp = False

def dfs(idx):
    global tmp
    if tmp:
        return

    if idx == len(lst):
        for row in arr:
            print(*row)
        tmp = True
        return

    for n in range(1, 10):
        i, j = lst[idx]
        if impossible_check(i, j, n):
            arr[i][j] = n
            dfs(idx + 1)
            arr[i][j] = 0

arr = [list(map(int, input().split())) for _ in range(9)]

lst = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            lst.append((i, j))

dfs(0)

    
