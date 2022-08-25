def dfs(idx, STK):
    global ans

    if n == idx:
        crs = 0
        for i in range(n):
            if STK[i] <= 0:
                crs += 1
        ans = max(crs, ans)
        return

    if STK[idx] > 0:

        for i in range(n):
            tmp = True
            if i != idx and STK[i] > 0:
                tmp = False
                stk = STK[:]
                stk[idx] -= w[i]
                stk[i] -= w[idx]
                dfs(idx+1, stk)
        if tmp:
            dfs(idx+1, STK)
    else:
        dfs(idx+1, STK)

n = int(input())
s = [0]*n
w = [0]*n
ans = 0
for i in range(n):
    s[i], w[i] = map(int, input().split())
dfs(0, s)

print(ans)

