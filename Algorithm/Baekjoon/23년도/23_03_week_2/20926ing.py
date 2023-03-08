import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def find_tera():
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'T':
                arr[i] = arr[i].replace('T', '0')
                return (i, j)

def sliding(h, w, i):
    t = 0
    dh, dw = D[i]
    nh = h+dh
    nw = w+dw
    while True:
        if H > nh >= 0 and W > nw >= 0:
            if arr[nh][nw] == 'R':
                return 'R', nh - dh, nw - dw, t
            elif arr[nh][nw] == 'H':
                return False
            elif arr[nh][nw] == 'E':
                return 'E', t
            else:
                t += int(arr[nh][nw])
                
        else:
            return False
        nh += dh
        nw += dw

def bfs(x, y, t):    
    global ans

    q = deque([(x, y, t, -1)])
    while q:
        h, w, t, path = q.popleft()
        if t >= ans:
            continue
        for i in range(4):
            if i == path | (i+2)%4 == path:
                continue
            nx = x + D[i][0]
            ny = y + D[i][1]
            if H > nx >= 0 and W > ny >= 0 and arr[nx][ny] != 'R':
                info = sliding(h, w, i)
                if info: 
                    if info[0] == 'R':
                        nh, nw, nt = info[1:]
                        q.append((nh, nw, t+nt, i))
                    else:
                        ans = min(ans, t + info[1])
            

D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
W, H = map(int, input().split())
arr = [input() for _ in range(H)]
ans = 10**7
x, y = find_tera()
path = {(x, y)}
bfs(x, y, 0)
if ans == 10**7:
    print(-1)
else:
    print(ans)


