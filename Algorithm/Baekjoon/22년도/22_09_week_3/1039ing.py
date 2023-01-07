N, K = input().split()
mx = int(N)
N = list(map(int, list(N)))
n_lst = sorted(N, reverse=True)
K = int(K)
idx = 0
if len(n_lst) == 1 or (n_lst[1] == 0 and len(n_lst) == 2):
    print(-1)
else:
    while K and idx < len(N):
        if N[idx] != n_lst[idx]:
            Mn_cnt = N[idx:].count(n_lst[idx])
            i = N[idx]
            i_cnt = 0
            for n in N[idx+1:idx+Mn_cnt]:
                if i > n:
                    i_cnt += 1
            for index, j in enumerate(N[::-1]):
                if j == n_lst[idx]:
                    if not i_cnt:
                        N[idx], N[-index - 1] = N[-index - 1], N[idx]
                        K -= 1
                        break
                    i_cnt -= 1
        idx += 1
    if K:
        if K%2 and len(N) == len(set(N)):
            N[-2], N[-1] = N[-1], N[-2]

    if N[0] == 0:
        print(-1)
    else:
        print(''.join(map(str, N)))
    