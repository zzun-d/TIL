import heapq
import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lst = []
for _ in range(N):
    S, E = map(int, input().split())
    heapq.heappush(lst, (E, S))

cnt = 0
while lst:
    nxt = []
    cnt += 1
    E = heapq.heappop(lst)[0]
    for _ in range(len(lst)):
        e, s = heapq.heappop(lst)
        if s >= E:
            E = e
        else:
            heapq.heappush(nxt, (e, s))
    lst = nxt[:]
print(cnt)