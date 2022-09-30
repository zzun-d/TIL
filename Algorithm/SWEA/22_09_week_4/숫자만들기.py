def operation(cnt, i, v):
    if i == 0:
        return v + nums[cnt]
    elif i == 1:
        return v - nums[cnt]
    elif i == 2:
        return v * nums[cnt]
    else:
        return int(v/nums[cnt])


def dfs(cnt, v):
    global mx, mn
    if cnt == N:
        if v > mx:
            mx = v
        if v < mn:
            mn = v
    else:
        for i in range(4):
            if oper[i]:
                oper[i] -= 1
                dfs(cnt+1, operation(cnt, i, v))
                oper[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    mx = -100000000
    mn = 100000000
    dfs(1, nums[0])
    print(f'#{tc} {mx-mn}')