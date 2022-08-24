N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
stack = [0]
ans = []
visited = [0]*N
while stack:
    if len(stack) == N:
        ans.append(stack)

    s = stack[-1]

    for i in range(1, N):
        if arr[s][i] and not visited[i]:
            stack.append(i)
            visited[i] = 1
            if len(stack) == N:
                ans.append(stack[:])
    else:
        stack.pop()


for path in ans:
    print(path)