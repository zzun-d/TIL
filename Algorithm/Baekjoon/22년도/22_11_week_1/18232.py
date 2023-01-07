from collections import deque, defaultdict

N, M = map(int, input().split())
S, E = map(int, input().split())
portal_dict = defaultdict(int)
visited = [0] * 300001
for _ in range(M):
    s, e = map(int, input().split())
    portal_dict[s] = e
queue = deque([S])
while queue:
    s = queue.popleft()

    if s == E:
        break

    if s < 30000 and visited[s+1] == 0:
        visited[s+1] = visited[s] + 1
        queue.append(s+1)
        
    if s > 0 and visited[s-1] == 0:
        visited[s-1] = visited[s] + 1
        queue.append(s-1)

    if portal_dict[s] and visited[portal_dict[s]] == 0:
        visited[portal_dict[s]] = visited[s] + 1
        queue.append(portal_dict[s])

print(visited[E])