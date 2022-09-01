

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[[] for _ in range(N)] for _ in range(N)]
cost_map = [[0]*N for _ in range(N)]
cnt = 0
mn_lst = []
mn = 20

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            d = 1
            while j+d < N and i+d < N:
                if arr[i+d][j+d] == 1:
                    visited[i][j].append((i+d, j+d))
                    cost_map[i][j] += 1
                d += 1

            d = 1
            while j+d < N and i-d >= 0:
                if arr[i-d][j+d] == 1:
                    visited[i][j].append((i-d, j+d))
                    cost_map[i][j] += 1
                d += 1

            d = 1
            while j-d >= 0 and i-d < N:
                if arr[i-d][j-d] == 1:
                    visited[i][j].append((i-d, j-d))
                    cost_map[i][j] += 1
                d += 1
                
            d = 1
            while j-d >= 0 and i+d < N:
                if arr[i+d][j-d] == 1:
                    visited[i][j].append((i+d, j-d))
                    cost_map[i][j] += 1
                d += 1
            if len(visited[i][j]) < mn:
                mn_lst = [(i, j)]
                mn = len(visited[i][j])
            elif len(visited[i][j]) == mn:
                mn_lst.append((i, j))
            
mi, mj = mn_lst.pop()  
mn_cost = visited[mi][mj]  
mmn_lst = [(mi, mj)]

while mn_lst:
    i, j = mn_lst.pop()
    if min([cost_map[ii][jj] for ii, jj in visited[i][j]]) > mn_cost:
        mn_cost = min([cost_map[ii][jj] for ii, jj in visited[i][j]])
        mmn_lst = [(i, j)]
    elif min([cost_map[ii][jj] for ii, jj in visited[i][j]]) == mn_cost:
        mmn_lst.append((i, j))
mi, mj = mmn_lst.pop()
mn_cost = visited[mi][mj]
mn_lst = [(mi, mj)]
while mmn_lst:
    i, j = mmn_lst.pop()
    if min([cost_map[ii][jj] for ii, jj in visited[i][j]]) < mn_cost:
        mn_cost = min([cost_map[ii][jj] for ii, jj in visited[i][j]])
        mn_lst = [(i, j)]
    

print(mn_lst)



