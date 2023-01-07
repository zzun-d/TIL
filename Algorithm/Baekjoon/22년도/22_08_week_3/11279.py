import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    cmd = int(input())
    if cmd:
        heapq.heappush(lst, -cmd)
    else:
        if lst:
            print(-heapq.heappop(lst))
        else:
            print(0)

    