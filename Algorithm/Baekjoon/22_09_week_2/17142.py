from itertools import combinations

def spread(virus, v):               # BFS로 바이러스 확산
    global pure_area, result
    cnt = 0
    while virus:
        nv = []
        for i, j in virus:
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] < 1 and not v[ni][nj]:
                    nv.append((ni, nj))
                    v[ni][nj] = 1
                    if arr[ni][nj] == 0:
                        pure_area -= 1
        # 유의점, 모든 청정구역이 바이러스로 오염됐고, 이번 턴에 확산 된 모든 지점이 비활성 바이러스 지역일 때 cnt는 올리지 않는다.
        if not pure_area:
            for ni, nj in nv:
                if arr[ni][nj] == 0:
                    cnt += 1
                    break
            result = min(cnt, result)
            break
        virus = nv[:]
        cnt += 1

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
V = []
area = 0

# 바이러스 array 생성(V에 좌표 append, 기존 값 2 -> -1)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            V.append([i, j])
            arr[i][j] = -1
        elif arr[i][j] == 0:
            area += 1

# 가능한 조합 리스트 생성
pos_virus = list(combinations(V, M))

# result 초기화
result = 2500

# 가능한 모든 경우의 수 탐색
for virus in pos_virus:
    for vi, vj in virus:
        arr[vi]
    visited = [[0] * N for _ in range(N)]
    pure_area = area
    spread(virus, visited)

if result == 2500:
    print(-1)
else:
    print(result)


