T = int(input())



for _ in range(T):
    N = int(input())
    lst = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12] + ([0]*N)
    if lst[N]:
        print(lst[N])
    else:
        for i in range(12, N+1):
            lst[i] += lst[i-1] + lst[i-5]
        print(lst[N])
    