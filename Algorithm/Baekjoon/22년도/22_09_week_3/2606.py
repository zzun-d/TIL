N = int(input())
visited =[0]*(N+1)
visited[1] = 1
cnt = 0
adjlst = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    adjlst[a].append(b)
    adjlst[b].append(a)

lst = [1]
while lst:

    for l in adjlst[lst.pop()]:
        if not visited[l]:
            visited[l] = 1
            lst.append(l)
            cnt += 1
print(cnt)