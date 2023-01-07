import sys
import heapq

input = sys.stdin.readline

p_min, p_max = [], []                   # 최소 heap, 최대 heap
visited = [0 for _ in range(100001)]    # 해당 문제 solved 한 난이도 저장
N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(p_min, (L, P))       # 최소 heap push
    heapq.heappush(p_max, (-L, -P))     # 최대 heap push
    visited[P] = L                      # 문제 난이도 저장
M = int(input())
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'recommend':               
        if cmd[1] == '1':       # 가장 어려운 난이도 추천
            while p_max:         # 최대 heap의 최댓값 문제가 solved 아니라면 break
                if visited[-p_max[0][1]] == -p_max[0][0]:
                    break
                else:           # 이미 solved 된 문제는 pop
                    heapq.heappop(p_max)
            print(-p_max[0][1])

        else:
            while p_min:        # 마찬가지
                if visited[p_min[0][1]] == p_min[0][0]:
                    break

                heapq.heappop(p_min)
            print(p_min[0][1])
    elif cmd[0] == 'add':       # add면 최대. 최소 heap에 (난이도, 번호)로 push
        heapq.heappush(p_min, (int(cmd[2]), int(cmd[1])))
        heapq.heappush(p_max, (-int(cmd[2]), -int(cmd[1])))
        visited[int(cmd[1])] = int(cmd[2])      # 해당 문제 난이도 갱신
    else:
        visited[int(cmd[1])] = 0    # 푼 문제 난이도 0으로 초기화

