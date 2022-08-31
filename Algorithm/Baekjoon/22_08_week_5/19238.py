di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

def bfs(q):
    nq = []
    while q:
        i, j = q.pop()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj]==0:
                nq.append([ni, nj])
    return nq


def search(queue, F):
    global ans
    if F <= 0:
        ans = -1
        return
    elif M == 0:
        ans = F
        return
    
    for c_info in client_infos:
        if si == c_info[0] and sj == c_info[1]:
            drive(c_info, F)
            return
    f = 0
    while queue:
        f += 1
        queue = bfs(queue)
        for c_info in client_infos:
            client_lst = []
            for n_q in queue:
                if n_q[0] == c_info[0] and n_q[1] == c_info[1]:
                    client_lst.append(c_info)
            if client_lst:
                client_lst.sort(reverse=True)
                drive(client_lst.pop(), F - f)
                return
        
def drive(C_INFO, F):
    global ans, M
    if F <= 0:
        ans = -1
        return
    ci, cj, gi, gj = C_INFO
    Q = [[ci, cj]]
    f = 0
    while Q:
        f += 1
        Q = bfs(Q)
        for NQ in Q:
            if NQ[0] == gi and NQ[1] == gj:
                if F >= f:
                    M -= 1
                    search([[gi, gj]], F + f)
                    return

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
si, sj = map(int, input().split())
client_infos = []
for _ in range(M):
    client_infos.append(list(map(int, input().split())))
print(client_infos)
visited = [[0]*N for _ in range(N)]
ans = 0
search([[si, sj]], F)
print(ans)