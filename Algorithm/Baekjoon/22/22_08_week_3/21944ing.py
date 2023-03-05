import sys
import heapq

input = sys.stdin.readline

p_min, p_max = [], []                   # 최소 heap, 최대 heap
p_g_min, p_g_max = [[] for _ in range(101)], [[] for _ in range(101)]
visited = [None for _ in range(100001)]    # 해당 문제 solved 한 난이도 저장
lv_pNum_max = [[] for _ in range(101)]
lv_pNum_min = [[] for _ in range(101)]
N = int(input())
for _ in range(N):
    P, L, G = map(int, input().split())
    heapq.heappush(p_min, (L, P, G))       # 최소 heap push
    heapq.heappush(p_max, (-L, -P, G))     # 최대 heap push
    heapq.heappush(p_g_min[G], (L, P, G))
    heapq.heappush(p_g_max[G], (-L, -P, G))
    heapq.heappush(lv_pNum_min[L], P)
    heapq.heappush(lv_pNum_max[L], -P)
    visited[P] = (L, G)                      # 문제 난이도, 알고리즘 저장
M = int(input())
for _ in range(M):
    
    cmd = input().split()
    if cmd[0] == 'recommend':
        cmd[1] = int(cmd[1])
        if cmd[2] == '1':       # 가장 어려운 난이도 추천
            while True:          # 최대 heap의 최댓값 문제가 solved 아니라면 break
                if visited[-p_g_max[cmd[1]][0][1]] == (-p_g_max[cmd[1]][0][0], p_g_max[cmd[1]][0][2]):
                    break
                else:           # 이미 solved 된 문제는 pop
                    heapq.heappop(p_g_max[cmd[1]])
            print(-p_g_max[cmd[1]][0][1])

        elif cmd[2] == '-1':
            while True:        # 마찬가지
                if visited[p_g_min[cmd[1]][0][1]] == (p_g_min[cmd[1]][0][0], p_g_min[cmd[1]][0][2]):
                    break

                else:
                    heapq.heappop(p_g_min[cmd[1]])

            print(p_g_min[cmd[1]][0][1])

    elif cmd[0] == 'recommend2':
        if cmd[1] == '1':
            while True:
                if visited[-p_max[0][1]] == (-p_max[0][0], p_max[0][2]):
                    break
                else:
                    heapq.heappop(p_max)
            print(-p_max[0][1])

        elif cmd[1] == '-1':
            while True:
                if visited[p_min[0][1]] == (p_min[0][0], p_min[0][2]):
                    break
                else:
                    heapq.heappop(p_min)
            print(p_min[0][1])

    elif cmd[0] == 'recommend3':
        L = int(cmd[2])
        if cmd[1] == '1':
            ans = -1
            for i in range(L, 101):
                while lv_pNum_min[i]:
                    if visited[lv_pNum_min[i][0]] != 0:
                        ans = lv_pNum_min[i][0]
                        break
                    else:
                        heapq.heappop(lv_pNum_min[i])
                if ans > 0:
                    break
            print(ans)
        elif cmd[1] == '-1':
            ans = -1
            for i in range(L-1, -1, -1):
                while lv_pNum_max[i]:
                    if visited[-lv_pNum_max[i][0]] != 0:
                        ans = -lv_pNum_max[i][0]
                        break
                    else:
                        heapq.heappop(lv_pNum_max[i])
                if ans > 0:
                    break
            print(ans)

    elif cmd[0] == 'add':       # add면 최대. 최소 heap에 (난이도, 번호)로 push
        P = int(cmd[1])
        L = int(cmd[2])
        G = int(cmd[3])
        heapq.heappush(p_min, (L, P, G))
        heapq.heappush(p_max, (-L, -P, G))
        heapq.heappush(p_g_min[G], (L, P, G))
        heapq.heappush(p_g_max[G], (-L, -P, G))
        heapq.heappush(lv_pNum_max[L], -P)
        heapq.heappush(lv_pNum_min[L], P)
        visited[P] = (L, G)      # 해당 문제 난이도 갱신
    elif cmd[0] == 'solved':
        visited[int(cmd[1])] = 0    # 푼 문제 난이도 0으로 초기화