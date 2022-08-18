import sys
import heapq

def solved_pop(heap, g=0, m=0, l=0):
    if g:
        while heap[g][m]:
            if visited[(-1**m)*heap[g][m][0][1]] == (-1**m)*heap[g][m][0][0]:
                break
            else:
                heapq.heappop(heap[g][m])
        return (-1**m)*heap[g][m][0][1], heap

    else:
        sub_heap = []
        while heap:
            if visited[(-1**m)*heap[0][1]] == (-1**m)*heap[0][0]:
                if (-1**m)*heap[0][0] < l:
                    heapq.heappush(sub_heap, heapq.heappop(heap))
                else:
                    break
            else:           
                heapq.heappop(heap)
        if sub_heap:
            heap = sub_heap + heap

        return (-1**m)*heap[0][1], sub_heap+heap

            
input = sys.stdin.readline

heap_g = [[[], []] for _ in range(101)]     # 알고리즘 분류 별 heap 생성
visited = [0 for _ in range(100001)]        # 해당 문제 solved 한 난이도 저장
p_max, p_min = [], []
N = int(input())
for _ in range(N):
    P, L, G = map(int, input().split())
    heapq.heappush(heap_g[G][0], (L, P))       # 최소 heap push
    heapq.heappush(heap_g[G][1], (-L, -P))     # 최대 heap push
    heapq.heappush(p_min, (L, P))
    heapq.heappush(p_max, (-L, -P))
    visited[P] = L                    # 문제 난이도 저장
M = int(input())
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'recommend':
        if cmd[2] == '1':       # 가장 어려운 난이도 추천
            ans, heap_g = solved_pop(heap_g, g=int(cmd[1]), m=1)
            print(ans)
        else:                   # 마찬가지
            ans, heap_g = solved_pop(heap_g, g=int(cmd[1]), m=0)
            print(ans)

    elif cmd[0] == 'recommend2':
        if cmd[1] == '1':
            ans, p_max = solved_pop(p_max, m=1)
            print(ans)
        else:
            ans, p_min = solved_pop(p_min, m=0)
            print(ans)
    
    elif cmd[0] == 'recommend3':
        if cmd[1] == '1':
            ans, p_min = solved_pop(p_min, m=0, l=int(cmd[2])+1)
            print(ans)
        else:
            ans, p_max = solved_pop(p_max, m=1, l=int(cmd[2]))
            print(ans)

    elif cmd[0] == 'add':       # add면 최대. 최소 heap에 (난이도, 번호)로 push
        heapq.heappush(heap_g[int(cmd[3])][0], (int(cmd[2]), int(cmd[1])))       # 최소 heap push
        heapq.heappush(heap_g[int(cmd[3])][1], (-int(cmd[2]), -int(cmd[1])))     # 최대 heap push
        heapq.heappush(p_min, (int(cmd[2]), int(cmd[1])))
        heapq.heappush(p_max, (-int(cmd[2]), -int(cmd[1])))
        visited[int(cmd[1])] = int(cmd[2])      # 해당 문제 난이도 갱신
    else:
        visited[int(cmd[1])] = 0    # 푼 문제 난이도 0으로 초기화

