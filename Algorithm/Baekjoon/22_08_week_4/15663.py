N, M = map(int, input().split())
l = input().split()

result = []
cnt = 0
ans = ''
visited = [False] * N

def dfs():
    global ans, cnt
    if cnt == M:
        result.append(tuple(map(int, ans[:].split())))
        return
        
    for i in range(N):
        if not visited[i]:
            if ans:
                ans += ' ' + l[i]
            else:
                ans = l[i]
            cnt += 1 
            visited[i] = True
            dfs()
            ans = ans[:-(len(l[i])+1)]
            cnt -= 1
            visited[i] = False

dfs()

result = list(set(result))
result.sort()

for r in result:
    print(*r)