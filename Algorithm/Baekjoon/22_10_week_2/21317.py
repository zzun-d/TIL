N = int(input())
dp1 = [0]*N
dp2 = [0]*N
lst = [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(lst[0][0])
elif N == 3:
    print(min(lst[0][1], lst[0][0] + lst[1][0]))
else:
    dp1[1] = lst[0][0]
    dp1[2] = min(lst[0][1], lst[0][0] + lst[1][0])
    for i in range(3, N):
        dp1[i] = min(dp1[i-1] + lst[i-1][0], dp1[i-2] + lst[i-2][1])
        dp2[i] = dp1[i-3] + K
        if dp2[i-1]:
            dp2[i] = min(dp2[i], dp2[i-1]+lst[i-1][0])
        if dp2[i-2]:
            dp2[i] = min(dp2[i], dp2[i-2]+lst[i-2][1])

    print(min(dp1[-1], dp2[-1]))
