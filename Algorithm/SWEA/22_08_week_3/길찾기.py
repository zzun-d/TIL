for _ in range(10):
    t, n = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, n*2, 2):
        graph[nums[i]].append(nums[i+1])
    visited = [True] + [False] * 100
    ans = v = 0
    stack = []
    while True:
        for w in graph[v]:
            if w == 99:
                ans = 1
                break
            elif not visited[w]:
                visited[w] = True
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                ans = 0
                break
        if ans:
            break
    print(f'#{t} {ans}')
