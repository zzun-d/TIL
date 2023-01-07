from collections import defaultdict
import sys


def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tmp = False
for i in range(N):
    friends = set([i])
    for j in graph[i]:
        if j not in friends:
            friends.add(j)
            for k in graph[j]:
                if k not in friends:
                    friends.add(k)
                    for l in graph[k]:
                        if l not in friends:
                            friends.add(l)
                            for m in graph[l]:
                                if m not in friends:
                                    tmp = True
                                    break
                            friends -= {l}
                        if tmp:
                            break
                    friends -= {k}
                if tmp:
                    break
            friends -= {j}
        if tmp:
            break
    if tmp:
        break
    friends -= {i}


if tmp:
    print(1)
else:
    print(0)

