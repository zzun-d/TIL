def dfs(stack, smp, V):
    global good_p
    # 종료조건, 스택이 비었을 때
    if not stack:
        return

    for i in range(1, N):
        p = arr[stack[-1]][i]
        if i not in stack and p and not V[i]:
            stack.append(i)
            V[i] = 1
            if len(stack) == N and arr[stack[-1]][0]:
                sm = arr[stack[-2]][stack[-1]] + smp + arr[stack[-1]][0]
                if good_p > sm:
                    good_p = sm

            dfs(stack, smp+p, V)
            V[i] = 0
            stack.pop()

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
good_p = 10000000
dfs([0], 0, visited)
print(good_p)

