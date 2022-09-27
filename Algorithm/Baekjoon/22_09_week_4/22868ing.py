from collections import defaultdict
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
visited = [0]*(N+1)
tree = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

s, e = map(int, input().split())
visited[s] = 1
tmp = False

def bfs1(lst, v):
    global tmp
    if tmp:
        pass

    elif e in lst:
        v[e] = 1
        tmp = True
        return v

    else:
        lst.sort(reverse=True)
        while lst and not tmp:
            n = lst.pop()
            if not v[n]:
                v[n] = 1
                bfs1(tree[n], v[:])
                v[n] = 0


def bfs2(lst, v):
    global tmp
    if tmp:
        return

    if s in lst:
        tmp = True
        return v
    lst.sort(reverse=True)

    while lst and not tmp:
        n = lst.pop()
        if not v[n]:
            v[n] = 1
            bfs1(tree[n], v[:])
            v[n] = 0

v2 = bfs1(tree[s], visited)
tmp =False
result = bfs2(tree[e], v2)
print(sum(result))