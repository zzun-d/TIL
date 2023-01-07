import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    h_max, h_min = [], []
    need_del = [False] * n
    for i in range(n):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(h_min, (num, i))
            heapq.heappush(h_max, (-num, i))
            need_del[i] = True
        elif num < 0:
            while h_min and not need_del[h_min[0][1]]:
                heapq.heappop(h_min)
            if h_min:
                need_del[h_min[0][1]] = False
                heapq.heappop(h_min)
        else:
            while h_max and not need_del[h_max[0][1]]:
                heapq.heappop(h_max)
            if h_max:
                need_del[h_max[0][1]] = False
                heapq.heappop(h_max)

    while h_min and not need_del[h_min[0][1]]:
        heapq.heappop(h_min)
    while h_max and not need_del[h_max[0][1]]:
        heapq.heappop(h_max)
    if h_max and h_min:
        mn = heapq.heappop(h_min)[0]
        mx = heapq.heappop(h_max)[0] * (-1)
        print(mx, mn)
    else:
        print('EMPTY')