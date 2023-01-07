import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap_m = []     # 음수 담을 heap
heap_p = []     # 양수 담을 heap
for _ in range(N):
    num = int(input())
    if num > 0:                         # 양수면 heap_p에 push
        heapq.heappush(heap_p, num)
    elif num < 0:                       # 음수면 - 곱해서 heap_m에 push
        heapq.heappush(heap_m, -num)
    else:                               # 0 이면 출력
        if heap_m and heap_p:               # heap_m, heap_p 둘다 존재 시 첫 원소 비교 후 낮은 거 출력               
            if heap_m[0] > heap_p[0]:
                print(heapq.heappop(heap_p))
            else:
                print(-heapq.heappop(heap_m))
        elif heap_m:                        # heap_m만 존재 시 heap_m heappop에 -곱해서 출력 
            print(-heapq.heappop(heap_m))
        elif heap_p:                        # heap_p만 존재 시 heap_p heappop
            print(heapq.heappop(heap_p))
        else:                               # 둘다 없으면 0 출력
            print(0)
