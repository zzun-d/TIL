N, K = map(int, input().split())
stack = []
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            stack.append((arr[i][j], i, j))
s, x, y = map(int, input().split())
stack.sort(reverse=True)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
n_stack = []
for _ in range(s):
    
    while stack:
        num, i, j = stack.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                arr[ni][nj] = num
                n_stack.append((num, ni, nj))
    n_stack.sort(reverse=True)
    stack = n_stack
    n_stack = []

print(arr[x-1][y-1])
