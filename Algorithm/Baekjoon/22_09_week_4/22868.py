from collections import defaultdict, deque
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
answer = 0
visited = {s}
queue = deque([({s}, sorted(tree[s]))])
while queue:
    path, nxt = queue.popleft()
    if set(nxt).intersection({e}):
        path.add(e)
        visited2 = path
        answer += len(path)
        break

    for n in nxt:
        if not visited.intersection({n}):
            visited |= {n}
            nnxt = sorted(list(set(tree[n]) - visited))
            if nnxt:
                queue.append((path|{n}, nnxt))
            else:
                visited -= {n}

queue = deque([({e}, sorted(tree[e]))])
visited2 -= {s}
while queue:
    path, nxt = queue.popleft()
    if set(nxt).intersection({s}):
        answer += len(path)
        break

    for n in nxt:
        if not visited2.intersection({n}):
            visited2 |= {n}
            nnxt = sorted(list(set(tree[n]) - visited2))
            if nnxt:
                queue.append((path|{n}, nnxt))
            else:
                visited2 -= {n}
print(answer-1)


