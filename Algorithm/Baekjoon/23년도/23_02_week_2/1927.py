import heapq, sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

q = []
ans = []
for _ in range(N):
    n = int(input())
    if n:
        heapq.heappush(q, n)
    elif q:
        print(heapq.heappop(q))
    else:
        print(0)