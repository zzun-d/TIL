import sys
from itertools import combinations
input = sys.stdin.readline

def dfs(l):
    global lst
    global ans
    if len(l) == n:
        sm = 0
        for ls in alpha:
            if not ls - set(l):
                sm += 1
        ans = max(ans, sm)

    else:    

        for i in range(21):
            if visited[i] == 0:
                visited[i] = 1
                l.append(lst[i])
                dfs(l)
                visited[i] = 0
                l.pop()



N, K = map(int, input().split())
alpha = []
ans = 0
for _ in range(N):
    alpha.append(set(input()[4:-4]) - set(['a', 'n', 't', 'i', 'c']))
visited = [0] * 21
n = K - 5
lst = list('bdefghjklmopqrsuvwxyz')
lst = combinations(lst, n)
x = []
if n > 0:
    dfs(list())
    print(ans)

else:
    print(0)

