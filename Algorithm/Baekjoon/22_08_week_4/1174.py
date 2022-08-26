def dfs(i):
    if len(lst) >= N:
        return lst[N-1]
    K = 10
    for i in range(5, 0, -1):
        if (K - i//(10**i)) > 0:
            K = (K - i//(10**i))
        else:







N = int(input())
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]