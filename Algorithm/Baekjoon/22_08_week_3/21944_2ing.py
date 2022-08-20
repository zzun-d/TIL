import sys
import heapq

input = sys.stdin.readline

L_heap = [[[], []] for _ in range(101)]     # 난이도 별 최소힙, 최대힙 저장
G_heap = [[[], []] for _ in range(101)]     # 알고리즘 별 최소힙, 최대힙 저장
P_visited = [[] for _ in range(100001)]        # 문제 풀이 여부를 난이도, 알고리즘으로 저장
N = int(input())

for _ in range(N):

    P, L, G = map(int, input().split())
    
    heapq.heappush(L_heap[L][0], (P, G))   
    heapq.heappush(L_heap[L][1], (-P, G))   
    heapq.heappush(G_heap[G][0], (L, P))   
    heapq.heappush(G_heap[G][1], (-L, -P))   
    P_visited[P] = (L, G)                      # 문제 난이도, 알고리즘 저장

M = int(input())

for _ in range(M):
    
    cmd = input().split()

    if cmd[0] == 'recommend':

        G = int(cmd[1])

        if cmd[2] == '1':       # 가장 어려운 난이도 추천
            while True:          # 최대 heap의 최댓값 문제가 solved 아니라면 break
                if P_visited[-G_heap[G][1][0][1]] == (-G_heap[G][1][0][0], G):
                    break
                else:           # 이미 solved 된 문제는 pop
                    heapq.heappop(G_heap[G][1])
            print(-G_heap[G][1][0][1])

        else:
            while True:        # 마찬가지
                if P_visited[G_heap[G][0][0][1]] == (G_heap[G][0][0][0], G):
                    break
                else:           # 이미 solved 된 문제는 pop
                    heapq.heappop(G_heap[G][0])
            print(G_heap[G][0][0][1])


    elif cmd[0] == 'recommend2':

        if cmd[1] == '1':
            i = 100
            while i > 0:
                if L_heap[i][1]:
                    if P_visited[-L_heap[i][1][0][0]] == (i, L_heap[i][1][0][1]):
                        break
                    else:
                        heapq.heappop(L_heap[i][1])
                else:
                    i -= 1
            print(-L_heap[i][1][0][0])    

        else:
            i = 1
            while i < 101:
                if L_heap[i][0]:
                    if P_visited[L_heap[i][0][0][0]] == (i, L_heap[i][0][0][1]):
                        break
                    else:
                        heapq.heappop(L_heap[i][0])
                else:
                    i += 1
            print(L_heap[i][0][0][0])

    elif cmd[0] == 'recommend3':

        L = int(cmd[2])

        if cmd[1] == '1':
            ans = -1
            for i in range(L, 101):
                if L_heap[i][0]:
                    if P_visited[L_heap[i][0][0][0]] == (i, L_heap[i][0][0][1]):
                        ans = L_heap[i][0][0][0]
                        break
                    else:
                        heapq.heappop(L_heap[i][0])
            print(ans)

        else:
            ans = -1
            for i in range(L-1, 0, -1):
                if L_heap[i][1]:
                    if P_visited[-L_heap[i][1][0][0]] == (i, L_heap[i][1][0][1]):
                        ans = -L_heap[i][1][0][0]
                        break
                    else:
                        heapq.heappop(L_heap[i][1])
            print(ans)


    elif cmd[0] == 'add':       # add면 최대. 최소 heap에 (난이도, 번호)로 push
        
        P, L, G = int(cmd[1]), int(cmd[2]), int(cmd[3])
        heapq.heappush(L_heap[L][0], (P, G))   
        heapq.heappush(L_heap[L][1], (-P, G))   
        heapq.heappush(G_heap[G][0], (L, P))   
        heapq.heappush(G_heap[G][1], (-L, -P))   
        P_visited[P] = (L, G)      # 해당 문제 난이도 갱신

    else:
        P = int(cmd[1])
        P_visited[P] = False    # 푼 문제 난이도 0으로 초기화