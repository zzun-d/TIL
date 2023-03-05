import sys
from heapq import heappop, heappush
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

graph = defaultdict(set)
comp = []
stack = []
graph[0] = {i for i in range(1, N+1)}
for _ in range(N):
    n, c, r = map(int, input().split())
    heappush(comp, (c-r, c+r, n))
S, E = map(int, input().split())
stack.append(heappop(comp))
while comp:
    l, r, c = heappop(comp)
    while stack:
        L, R, C = stack[-1]
        if l < R:
            graph[C].add(c)
            stack.append((l, r, c))
            break
        else:
            stack.pop()
    stack.append((l, r, c))
    if not comp:
        graph[c] = set()
ans = [S]
ans2 = [E]
s = S
e = E
tmp = True
post = pre = True
while tmp and (post or pre):
    if pre:
        for k, v in list(graph.items())[::-1]:
            if v.intersection({s}):
                ans.append(k)
                s = k
                if s == 0:
                    pre = False
                elif graph[s].intersection({E}):
                    ans.append(E)
                    tmp = False

                break

    if post:
        for k, v in list(graph.items())[::-1]:
            if v.intersection({e}):
                ans2.append(k)
                e = k
                if e == 0:
                    post = False
                elif graph[e].intersection({S}):
                    ans2.append(S)
                    tmp = False

                break

if ans[-1] == 0:
    print(len(ans) + len(ans2) - 1)
    print(*ans, *ans2[::-1][1:])
else:
    print(len(ans))
    print(*ans)