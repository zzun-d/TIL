from collections import defaultdict, deque


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = defaultdict(list)
    dp = [0] + [10000]*(N)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    queue = deque([0])
    while queue:
        n = queue.popleft()
        for w, e in graph[n]:
            if dp[n] + w < dp[e]:
                dp[e] = dp[n] + w
                queue.append(e)
    print(f'#{tc} {dp[N]}')
