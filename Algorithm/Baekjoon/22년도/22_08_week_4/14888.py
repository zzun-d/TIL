def dfs(l):
    if sum(cal) == 0:
        lst.append(l)
        return
    for i in range(4):
        if cal[i]:
            cal[i] -= 1
            l.append(i+1)
            dfs(l[:])
            l.pop()
            cal[i] += 1

N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split()))
lst = []
dfs([])
answer = []

for l in lst:
    ans = A[0]
    for i in range(N-1):
        if l[i] == 1:
            ans += A[i+1]
        elif l[i] == 2:
            ans -= A[i+1]
        elif l[i] == 3:
            ans *= A[i+1]
        else:
            if ans >= 0:
                ans = ans // A[i+1]
            else:
                ans = -((-ans)//A[i+1])
    answer.append(ans)
print(max(answer))
print(min(answer))
