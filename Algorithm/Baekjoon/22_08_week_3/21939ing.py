import sys
import heapq

input = sys.stdin.readline
p_min, p_max = [], []
visited = [0] * 100001
N = int(input())
for _ in range(N):
    p_num, imp = map(int, input().split())
    heapq.heappush(p_min, (imp, p_num))
    heapq.heappush(p_max, (-imp, p_num))
    visited[p_num] = imp
M = int(input())
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'recommend':
        if cmd[1] == '1':
            i = 1
            ln = 0
            while len(p_max) > i and p_max[ln][0] == p_max[i][0]:
                if p_max[i][1] > p_max[ln][1]:
                    ln = i
                i += 1
            print(p_max[ln][1])
        else:
            print(p_min[0][1])
    elif cmd[0] == 'add':
        heapq.heappush(p_min, (int(cmd[2]), int(cmd[1])))
        heapq.heappush(p_max, (-int(cmd[2]), int(cmd[1])))
        visited[int(cmd[1])] = int(cmd[2])
    else:
        p_max.remove((-visited[int(cmd[1])], int(cmd[1])))
        p_min.remove((visited[int(cmd[1])], int(cmd[1])))
        heapq.heappush(p_max, (-101, 0))
        heapq.heappush(p_min, (-101, 0))
        heapq.heappop(p_max)
        heapq.heappop(p_min)
        visited[int(cmd[1])] = 0

