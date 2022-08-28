dij = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(p):
    global cnt

    if N == len(stack):
        cnt += len(stack[-1])
        stack.pop()
        stack[-1].pop()
        return
    i = len(stack)
    j = 
    n_p = []
    for d in dij:
        pass

N = int(input())
place = [[0]*N for _ in range(N)]
cnt = 0
stack = []

dfs(visited)