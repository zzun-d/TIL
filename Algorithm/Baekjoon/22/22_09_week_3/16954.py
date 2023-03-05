arr = [list(input()) for _ in range(8)]     # 8x8 맵
queue = [(7, 0)]                            # 욱제위치(맨 아래 왼쪽)
tmp = False                                 # 욱제의 목적지 도달 여부

while queue and not tmp:                # 욱제가 움직일 수 있는 공간이 있고, 목적지에 도달하지 않았다면,
    nxt = set()                             # 다음 이동 가능 후보(set을 이용하여 중복 제거)
    for _ in range(len(queue)):                 # bfs
        i, j = queue.pop()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 8 and 0 <= nj < 8 and arr[ni][nj] == '.':      # 다음 좌표가 맵 내에 있으며, 벽이 아니면 일단 후보
                if ni > 0 and arr[ni-1][nj] == '#':                         # 후보 좌표의 상단이 존재하며 벽일 때, 후보 박탈
                    continue
                elif ni == 0 and nj == 7:                                   # 만약 목적지에 도달하였으면 tmp 갱신
                    tmp = True
                    break
                nxt.add((ni, nj))                                           # 목적지가 아닌 이동 가능 좌표면 nxt에 추가

    arr.pop()                   # 맵의 최 하단 삭제                                                
    arr = [['.']*8] + arr       # 맵의 최 상단 빈칸으로 추가  => 벽이 내려오는 효과
    queue = list(nxt)           # queue 갱신

    if tmp:
        break
    
if tmp:
    print(1)
else:
    print(0)