import heapq
import sys
def input():
    return sys.stdin.readline().rstrip()
    
T = int(input())
for tc in range(1, T+1):
    K = int(input())
    lst = list(map(int, input().split()))
    heapq.heapify(lst)
    ans = 0
    for _ in range(K-1):
        a = heapq.heappop(lst) + heapq.heappop(lst)
        ans += a
        heapq.heappush(lst, a)
    print(ans)
