N, M = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
ans = []

def dfs():
    if len(ans) == M:
        print(*ans)
        return
    
    for i in l:
        ans.append(i)
        dfs()
        ans.pop()

dfs()