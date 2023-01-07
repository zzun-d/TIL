import sys
import heapq

input = sys.stdin.readline

L_min = [[] for _ in range(101)]
L_max = [[] for _ in range(101)]
G_min = [[] for _ in range(101)]
G_max = [[] for _ in range(101)]
P_visited = [[] for _ in range(100001)]  # 문제 풀이 여부 저장
N = int(input())

for _ in range(N):
    P, L, G = map(int, input().split())
    lp = P * 1000
    gl = L * 1000000
    vl = L * 1000
    heapq.heappush(L_min[L], lp+G)  # 난이도 별 최소힙에 (문제번호, 알고리즘 유형)으로 push
    heapq.heappush(L_max[L], -(lp+G))  # 난이도 별 최소힙에 (문제번호, 알고리즘 유형)으로 push
    heapq.heappush(G_min[G], gl+P)
    heapq.heappush(G_max[G], -(gl+P))
    P_visited[P] = (L, G)  # 문제 풀이 여부 list에 (난이도, 알고리즘 유형) 저장 -> 이미 풀었던 문제가 다른 난이도와 유형으로 들어온 것인지 확인하기 위함

M = int(input())

for _ in range(M):

    cmd = input().split()

    if cmd[0] == 'recommend':  # recommend 명령,

        G = int(cmd[1])  # 알고리즘 유형

        if cmd[2] == '1':  # 가장 어려운 난이도 추천

            while True:  # 알고리즘 유형 별 난이도 최댓값에 해당하는 문제가 존재할 때까지 루프
                if P_visited[(-G_max[G][0])%1000000] == ((-G_max[G][0])//1000000, G):
                    break

                else:  # 이미 solved 된 문제는 pop
                    heapq.heappop(G_max[G])

            print((-G_max[G][0])%1000000)  # 루프를 빠져나오면 해당 최댓값 프린트

        else:
            while True:  # 마찬가지

                if P_visited[G_min[G][0]%1000000] == ((G_min[G][0])//1000000, G):
                    break

                else:
                    heapq.heappop(G_min[G])

            print(G_min[G][0]%1000000)


    elif cmd[0] == 'recommend2':  # recommend2 명령,

        if cmd[1] == '1':  # 가장 어려운 난이도 추천
            i = 100  # 최고 난이도 index

            while i > 0:  # 난이도 100부터 1까지 존재하는 문제 탐색
                if L_max[i]:  # 문제가 이미 푼 문제면 pop, and list에 원소 존재 하지 않으면 난이도 1 감소

                    if P_visited[(-L_max[i][0])//1000] == (i, (-L_max[i][0])%1000):
                        break

                    else:
                        heapq.heappop(L_max[i])

                else:
                    i -= 1

            print((-L_max[i][0])//1000)

        else:  # 마찬가지
            i = 1

            while i < 101:
                if L_min[i]:

                    if P_visited[L_min[i][0]//1000] == (i, L_min[i][0]%1000):
                        break

                    else:
                        heapq.heappop(L_min[i])

                else:
                    i += 1

            print(L_min[i][0]//1000)

    elif cmd[0] == 'recommend3':  # recommend3 명령,

        L = int(cmd[2])  # 기준 난이도

        if cmd[1] == '1':  # 기준 난이도 보다 같거나 큰 난이도 중 가장 쉬운 난이도의 문제 추천
            ans = -1  # ans default -1

            for i in range(L, 101):  # 기준 난이도 부터 최대 난이도인 100까지 루프

                if L_min[i]:  # 문제가 이미 푼 문제면 pop, and list에 원소 존재 하지 않으면 난이도 1 증가
                    # 문제가 존재하면 ans에 저장
                    if P_visited[L_min[i][0]//1000] == (i, L_min[i][0]%1000):
                        ans = L_min[i][0]//1000
                        break

                    else:
                        heapq.heappop(L_min[i])

            print(ans)

        else:  # 마찬가지
            ans = -1

            for i in range(L - 1, 0, -1):
                if L_max[i]:
                    if P_visited[(-L_max[i][0])//1000] == (i, (-L_max[i][0])%1000):
                        ans = (-L_max[i][0])//1000
                        break
                    else:
                        heapq.heappop(L_max[i])
            print(ans)


    elif cmd[0] == 'add':  # add 명령,

        # 각 힙에 문제정보 push, 문제풀이 여부 리스트 갱신
        P, L, G = map(int,cmd[1:])
        lp = P * 1000
        gl = L * 1000000
        vl = L * 1000
        heapq.heappush(L_min[L], lp+G)  # 난이도 별 최소힙에 (문제번호, 알고리즘 유형)으로 push
        heapq.heappush(L_max[L], -(lp+G))  # 난이도 별 최소힙에 (문제번호, 알고리즘 유형)으로 push
        heapq.heappush(G_min[G], gl+P)
        heapq.heappush(G_max[G], -(gl+P))
        P_visited[P] = (L, G)

    else:  # solved 명령,
        P = int(cmd[1])
        P_visited[P] = False  # 푼 문제 난이도 False로 초기화