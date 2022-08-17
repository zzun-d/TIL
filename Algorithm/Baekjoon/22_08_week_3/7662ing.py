import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for t in range(1, T+1):
    n = int(input())
    heap = []

    for _ in range(n):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(heap, num)
        else:
            if num < 0 and heap:
                heapq.heappop(heap)
            elif heap:
                heap.remove(max(heap))
    if heap:
        print(max(heap), heapq.heappop(heap))
    else:
        print('EMPTY')



# 시간초과...