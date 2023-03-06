from collections import defaultdict, deque

def f(n1, n2):
    q = deque(trees[n1])
    while q:
        node, distance = q.popleft()
        if node == n2:
            return distance
        for n, d in trees[node]:
            if visited[n] == False:
                visited[n] = True
                q.append((n, distance+d))
            


N, M = map(int, input().split())

trees = defaultdict(list)

for _ in range(N-1):
    p, c, d = map(int, input().split())
    trees[p].append((c, d))
    trees[c].append((p, d))


for _ in range(M):
    n1, n2 = map(int, input().split())
    visited = [False] * (N+1)
    print(f(n1, n2))