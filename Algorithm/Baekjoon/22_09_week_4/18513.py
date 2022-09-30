from collections import deque


q = deque()
visited = dict()

N, K = map(int, input().split())
sam = list((map(int, input().split())))

for s in sam:
    q.append(s)
    visited[s] = 0

while q:
    if K <= 0:
        break

    s = q.popleft()
    for x in [s-1, s+1]:
        if x not in visited and K > 0:
            visited[x] = visited[s] + 1
            K -= 1
            q.append(x)

result = 0
for k, v in visited.items():
    result += v
print(result)